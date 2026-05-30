import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, DateTime, Boolean
from faker import Faker 
from datetime import datetime

metadata_obj = MetaData()

users_table = sqlalchemy.Table(
        'users',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_name', String(50), unique=True, nullable=False),
        Column('password', String(255), nullable=False),
        Column('user_role', String(50), nullable=False),
        Column('email', String(120), unique=True, nullable=False),
        Column('created_at', DateTime, nullable=False),
        Column('is_active', Boolean, default=True)
    )

products_table = sqlalchemy.Table(
        'products',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('product_name', String(100), nullable=False),
        Column('price', Integer, nullable=False),
        Column('created_at', DateTime, nullable=False),
        Column('stock', Integer, nullable=False)
    )

invoices_table = sqlalchemy.Table(
        'invoices',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
        Column('total_price', Integer, nullable=False),
        Column('created_at', DateTime, nullable=False)
    )

invoice_details_table = sqlalchemy.Table(
        'invoice_details',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('invoice_id', Integer, ForeignKey('invoices.id'), nullable=False),
        Column('product_id', Integer, ForeignKey('products.id'), nullable=False),
        Column('quantity', Integer, nullable=False),
        Column('price', Integer, nullable=False),
        Column('total_price', Integer, nullable=False)
    )

def create_tables(dbEngine):
    metadata_obj.create_all(dbEngine)

def insert_initial_data(db_connection):

    faker = Faker('en_US')  

    initial_products = []

    for _ in range(10):
        product_name = faker.word().capitalize()
        price = faker.random_int(min=10, max=100)
        created_at = faker.date_time_this_year()
        stock = faker.random_int(min=1, max=50)

        initial_products.append({
            'product_name': product_name,
            'price': price,
            'created_at': created_at,
            'stock': stock
        })

    insert_products_query = products_table.insert().values(initial_products)
    db_connection.execute_statement(insert_products_query)

class User:

    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj


    def insert_user(self, user_name, password, user_role, email, created_at = None, is_active=True):
        if created_at is None:
            created_at = datetime.now()
        insert_query = self.metadata.tables['users'].insert().values(
            user_name=user_name,
            password=password,
            user_role=user_role,
            email=email,
            created_at=created_at,
            is_active=is_active
        ).returning(self.metadata.tables['users'].c.id)
        result = self.db.execute_statement(insert_query)
        return result[0][0] if result else None
    
    def get_user_by_id(self, user_id):
        select_query = self.metadata.tables['users'].select().where(self.metadata.tables['users'].c.id == user_id)
        result = self.db.execute_statement(select_query)
        return result[0] if result else None

    def get_user_by_credentials(self, user_name, password):
        select_query = self.metadata.tables['users'].select().where(
            (self.metadata.tables['users'].c.user_name == user_name) &
            (self.metadata.tables['users'].c.password == password)
        )
        result = self.db.execute_statement(select_query)
        return result[0] if result else None

class Products:
    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj

    def get_product_by_id(self, product_id):
        select_query = self.metadata.tables['products'].select().where(self.metadata.tables['products'].c.id == product_id)
        result = self.db.execute_statement(select_query)
        result_formatted = {'id': result[0][0], 'product_name': result[0][1], 'price': result[0][2], 'created_at': result[0][3], 'stock': result[0][4]} if result else None
        return result_formatted
    
    def get_all_products(self):
        select_query = self.metadata.tables['products'].select()
        result = self.db.execute_statement(select_query)
        formatted_result = [{'id': row[0], 'product_name': row[1], 'price': row[2], 'stock': row[4], 'created_at': row[3]} for row in result] if result else []
        return formatted_result
    
    def create_product(self, product_name, price, created_at = None, stock = 0):
        if created_at is None:
            created_at = datetime.now()
        insert_query = self.metadata.tables['products'].insert().values(
            product_name=product_name,
            price=price,
            created_at=created_at,
            stock=stock
        ).returning(self.metadata.tables['products'].c.id, self.metadata.tables['products'].c.product_name, self.metadata.tables['products'].c.price, self.metadata.tables['products'].c.stock, self.metadata.tables['products'].c.created_at)
        result = self.db.execute_statement(insert_query)
        formatted_result = {'id': result[0][0], 'product_name': result[0][1], 'price': result[0][2], 'stock': result[0][3], 'created_at': result[0][4]} if result else None
        return formatted_result
    
    def update_product(self, product_id, product_name=None, price=None, stock=None):
        update_values = {}
        if product_name is not None:
            update_values['product_name'] = product_name
        if price is not None:
            update_values['price'] = price
        if stock is not None:
            update_values['stock'] = stock
        
        if not update_values:
            return False  # No values to update

        update_query = self.metadata.tables['products'].update().where(
            self.metadata.tables['products'].c.id == product_id
        ).values(**update_values).returning(self.metadata.tables['products'].c.id, self.metadata.tables['products'].c.product_name, self.metadata.tables['products'].c.price, self.metadata.tables['products'].c.stock, self.metadata.tables['products'].c.created_at)
        
        result = self.db.execute_statement(update_query)
        formatted_result = {'id': result[0][0], 'product_name': result[0][1], 'price': result[0][2], 'stock': result[0][3], 'created_at': result[0][4]} if result else None
        return formatted_result

    def delete_product(self, product_id):
        delete_query = self.metadata.tables['products'].delete().where(self.metadata.tables['products'].c.id == product_id)
        self.db.execute_statement(delete_query)
    
class Invoice:
    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj

    def reduce_stock(self, product_list):
        stock_update_queries = []
        for product in product_list:
            update_query = self.metadata.tables['products'].update().where(
                self.metadata.tables['products'].c.id == product['id']
            ).values(stock=self.metadata.tables['products'].c.stock - product['quantity'])
            stock_update_queries.append(update_query)
        
        return stock_update_queries
    
    def create_invoice_details(self, invoice_id, product_list):
        invoice_details_queries = []
        for product in product_list:
            total_price = product['price'] * product['quantity']
            insert_query = self.metadata.tables['invoice_details'].insert().values(
                invoice_id=invoice_id,
                product_id=product['id'],
                quantity=product['quantity'],
                price=product['price'],
                total_price=total_price
            )
            invoice_details_queries.append(insert_query)
        
        return invoice_details_queries
    
    def delete_invoice(self, invoice_id):
        delete_invoice_query = self.metadata.tables['invoices'].delete().where(self.metadata.tables['invoices'].c.id == invoice_id)
        self.db.execute_statement(delete_invoice_query)

    def genetate_invoice(self, user_id, product_list):
        total_price = sum([product['price'] * product['quantity'] for product in product_list])
        insert_query = self.metadata.tables['invoices'].insert().values(
            user_id=user_id,
            total_price=total_price,
            created_at=datetime.now()
        ).returning(self.metadata.tables['invoices'].c.id)
        result = self.db.execute_statement(insert_query)
        invoice_id = result[0][0] if result else None

        try:

            if invoice_id:
                invoice_details_queries = self.create_invoice_details(invoice_id, product_list)
                stock_update_queries = self.reduce_stock(product_list)
                all_queries = invoice_details_queries + stock_update_queries
                self.db.execute_multiple_statements(all_queries)
            
                invoice_query = self.metadata.tables['invoices'].select().where(self.metadata.tables['invoices'].c.id == invoice_id)
                invoice_result = self.db.execute_statement(invoice_query)
                result_formatted = {'id': invoice_result[0][0], 'user_id': invoice_result[0][1], 'total_price': invoice_result[0][2], 'created_at': invoice_result[0][3]} if invoice_result else None
                return result_formatted
            raise Exception("Invoice ID not found after insertion.")
        
        except Exception as ex:
            self.delete_invoice(invoice_id)
            print(f"System error during the purchase process: {ex}")
            raise 
    
    def get_invoice_by_id(self, invoice_id):
        invoice_query = self.metadata.tables['invoices'].select().where(self.metadata.tables['invoices'].c.id == invoice_id)
        invoice_result = self.db.execute_statement(invoice_query)
        result_formatted_header = {'invoice': {'id': invoice_result[0][0], 'user_id': invoice_result[0][1], 'total_price': invoice_result[0][2], 'created_at': invoice_result[0][3]}} if invoice_result else None

        invoice_details_query = self.metadata.tables['invoice_details'].select().where(self.metadata.tables['invoice_details'].c.invoice_id == invoice_id)
        invoice_details_result = self.db.execute_statement(invoice_details_query)
        result_formatted_details = {'details': [{'id': row[0], 'invoice_id': row[1], 'product_id': row[2], 'quantity': row[3], 'price': row[4], 'total_price': row[5]} for row in invoice_details_result]} if invoice_details_result else {'details': []}
        return {**result_formatted_header, **result_formatted_details}
    
    def get_invoices_by_user_id(self, user_id):
        invoices_query = self.metadata.tables['invoices'].select().where(self.metadata.tables['invoices'].c.user_id == user_id)
        invoices_result = self.db.execute_statement(invoices_query)
        result_formatted_invoices = []
        if invoices_result:
            for invoice in invoices_result:
                invoice_id = invoice[0]
                invoice_details_query = self.metadata.tables['invoice_details'].select().where(self.metadata.tables['invoice_details'].c.invoice_id == invoice_id)
                invoice_details_result = self.db.execute_statement(invoice_details_query)
                result_formatted_details = [{'id': row[0], 'invoice_id': row[1], 'product_id': row[2], 'quantity': row[3], 'price': row[4], 'total_price': row[5]} for row in invoice_details_result] if invoice_details_result else []
                result_formatted_invoices.append({'invoice': {'id': invoice[0], 'user_id': invoice[1], 'total_price': invoice[2], 'created_at': invoice[3]}, 'details': result_formatted_details})
        return result_formatted_invoices
