import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, DateTime, Boolean
from faker import Faker 

metadata_obj = MetaData()

user_table = sqlalchemy.Table(
        'users',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_name', String(50), unique=True, nullable=False),
        Column('email', String(120), unique=True, nullable=False),
        Column('created_at', DateTime, nullable=False),
        Column('is_active', Boolean, default=True)
    )

address_table = sqlalchemy.Table(
        'addresses',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey("users.id"), nullable=False),
        Column('address_line', String(200), nullable=False),
        Column('city', String(50), nullable=False),
        Column('state', String(50), nullable=False),
        Column('zip_code', String(10), nullable=False)
    )

car_table = sqlalchemy.Table(
        'cars',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey("users.id"), nullable=True),
        Column('brand', String(50), nullable=False),
        Column('model', String(50), nullable=False),
        Column('year', Integer, nullable=False),
        Column('is_available', Boolean, default=True)
    )

def create_tables(dbEngine):
    metadata_obj.create_all(dbEngine)

def insert_initial_data(db_connection):

    faker = Faker('en_US')  

    initial_users = []

    for _ in range(20):
        user_name = faker.user_name()
        email = faker.email()
        created_at = faker.date_time_this_decade()
        initial_users.append({"user_name": user_name, "email": email, "created_at": created_at})
    
    insert_users_stmt = metadata_obj.tables['users'].insert().values(initial_users)

    initial_addresses = []

    for i in range(1, 21):
        user_id = i
        address_line = faker.street_address()
        city = faker.city()
        state = faker.state_abbr()
        zip_code = faker.zipcode()
        initial_addresses.append({"user_id": user_id, "address_line": address_line, "city": city, "state": state, "zip_code": zip_code})


    insert_addresses_stmt = metadata_obj.tables['addresses'].insert().values(initial_addresses)

    initial_cars = []

    for i in range(30):
        user_id = faker.random_element(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None])
        brand = faker.random_element(elements=["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Hyundai", "Kia", "Volkswagen", "Mazda", "Subaru"])
        model = faker.word().capitalize()
        year = faker.year()
        is_available = faker.boolean()
        initial_cars.append({"user_id": user_id, "brand": brand, "model": model, "year": year, "is_available": is_available})

    insert_cars_stmt = metadata_obj.tables['cars'].insert().values(initial_cars)

    db_connection.execute_multiple_statements([insert_users_stmt, insert_addresses_stmt, insert_cars_stmt])


class User:

    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj

    def get_info_by_user_id(self, user_id):

        cars = Cars(self.db)
        addresses = User(self.db)
        
        # Get cars for a specific user
        user_cars = cars.get_car(user_id=user_id)
        print(f"Cars for User ID {user_id}:", user_cars)

        # Get addresses for a specific user
        user_addresses = addresses.get_address(user_id=user_id)
        print(f"Addresses for User ID {user_id}:", user_addresses)


    def get_user(self, **filters):
        try:
            select_stmt = self.metadata.tables['users'].select().where(
                sqlalchemy.and_(*[getattr(self.metadata.tables['users'].c, key) == value for key, value in filters.items()])
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching user: {e}")
            raise
        
    def get_users_with_multiple_cars(self):
        try:
            select_stmt = self.metadata.tables['users'].select().join(
                self.metadata.tables['cars'],
                self.metadata.tables['users'].c.id == self.metadata.tables['cars'].c.user_id
            ).group_by(
                self.metadata.tables['users'].c.id
            ).having(
                sqlalchemy.func.count(self.metadata.tables['cars'].c.id) > 1
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching users with multiple cars: {e}")
            raise

    def create_user(self, user_name, email, created_at, is_active=True):
        try:
            insert_stmt = self.metadata.tables['users'].insert().values(
                user_name=user_name,
                email=email,
                created_at=created_at,
                is_active=is_active
            ).returning(self.metadata.tables['users'].c.id, self.metadata.tables['users'].c.user_name, self.metadata.tables['users'].c.email, self.metadata.tables['users'].c.created_at, self.metadata.tables['users'].c.is_active)
            return self.db.execute_statement(insert_stmt)
        except Exception as e:
            print(f"Error creating user: {e}")
                
        
    def update_user(self, user_id, **updates):
        try:
            update_stmt = self.metadata.tables['users'].update().where(
                self.metadata.tables['users'].c.id == user_id
            ).values(**updates).returning(self.metadata.tables['users'].c.id, self.metadata.tables['users'].c.user_name, self.metadata.tables['users'].c.email, self.metadata.tables['users'].c.created_at, self.metadata.tables['users'].c.is_active)
            return self.db.execute_statement(update_stmt)
        except Exception as e:
            print(f"Error updating user: {e}")
            raise
        
    def delete_user(self, user_id):
        try:
            delete_stmt = self.metadata.tables['users'].delete().where(
                self.metadata.tables['users'].c.id == user_id
            )
            self.db.execute_statement(delete_stmt)
            return "User with id " + str(user_id) + " deleted"
        except Exception as e:
            print(f"Error deleting user: {e}")
            raise
        
    def addresses(self, user_id):
        try:
            select_stmt = self.metadata.tables['addresses'].select().where(
                self.metadata.tables['addresses'].c.user_id == user_id
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching addresses for user: {e}")
            raise   
        
    def cars(self, user_id):
        try:
            select_stmt = self.metadata.tables['cars'].select().where(
                self.metadata.tables['cars'].c.user_id == user_id
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching cars for user: {e}")
            raise

class Address:

    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj

    def get_address(self, **filters):
        try:
            select_stmt = self.metadata.tables['addresses'].select().where(
                sqlalchemy.and_(*[getattr(self.metadata.tables['addresses'].c, key) == value for key, value in filters.items()])
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching address: {e}")
            raise
        
    def get_addresses_with_string(self, substring):
        try:
            select_stmt = self.metadata.tables['addresses'].select().where(
                self.metadata.tables['addresses'].c.address_line.ilike(f"%{substring}%")
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching addresses with substring '{substring}': {e}")
            raise
        
    def create_address(self, user_id, address_line, city, state, zip_code):
        try:
            insert_stmt = self.metadata.tables['addresses'].insert().values(
                user_id=user_id,
                address_line=address_line,
                city=city,
                state=state,
                zip_code=zip_code
            ).returning(
                self.metadata.tables['addresses'].c.id,
                self.metadata.tables['addresses'].c.user_id,
                self.metadata.tables['addresses'].c.address_line,
                self.metadata.tables['addresses'].c.city,
                self.metadata.tables['addresses'].c.state,
                self.metadata.tables['addresses'].c.zip_code
            )
            return self.db.execute_statement(insert_stmt)
        except Exception as e:
            print(f"Error creating address: {e}")
            raise
        
    def update_address(self, address_id, **updates):
        try:
            update_stmt = self.metadata.tables['addresses'].update().where(
                self.metadata.tables['addresses'].c.id == address_id
            ).values(**updates).returning(self.metadata.tables['addresses'].c.id, self.metadata.tables['addresses'].c.user_id, self.metadata.tables['addresses'].c.address_line, self.metadata.tables['addresses'].c.city, self.metadata.tables['addresses'].c.state, self.metadata.tables['addresses'].c.zip_code)
            return self.db.execute_statement(update_stmt)
        except Exception as e:
            print(f"Error updating address: {e}")
            raise
        
    def delete_address(self, address_id):
        try:
            delete_stmt = self.metadata.tables['addresses'].delete().where(
                self.metadata.tables['addresses'].c.id == address_id
            )
            self.db.execute_statement(delete_stmt)
            return "Address with id " + str(address_id) + " deleted"
        except Exception as e:
            print(f"Error deleting address: {e}")
            raise
        
class Cars:

        def __init__(self,db_connection):
            self.db = db_connection
            self.metadata = metadata_obj

        def get_car(self, **filters):
            try:
                select_stmt = self.metadata.tables['cars'].select().where(
                    sqlalchemy.and_(*[getattr(self.metadata.tables['cars'].c, key) == value for key, value in filters.items()])
                )
                return self.db.execute_statement(select_stmt)
            except Exception as e:
                print(f"Error fetching car: {e}")
                raise
            
        def get_cars_without_user(self):
            try:
                select_stmt = self.metadata.tables['cars'].select().where(
                    self.metadata.tables['cars'].c.user_id.is_(None)
                )
                return self.db.execute_statement(select_stmt)
            except Exception as e:
                print(f"Error fetching cars without user: {e}")
                raise
            
        def create_car(self, brand, model, year, is_available=True, user_id = None):
            try:
                insert_stmt = self.metadata.tables['cars'].insert().values(
                    brand=brand,
                    model=model,
                    year=year,
                    is_available=is_available,
                    user_id=user_id
                ).returning(self.metadata.tables['cars'].c.id, self.metadata.tables['cars'].c.brand, self.metadata.tables['cars'].c.model, self.metadata.tables['cars'].c.year, self.metadata.tables['cars'].c.is_available, self.metadata.tables['cars'].c.user_id)
                return self.db.execute_statement(insert_stmt)
            except Exception as e:
                print(f"Error creating car: {e}")
                raise
            
        def update_car(self, car_id, **updates):
            try:
                update_stmt = self.metadata.tables['cars'].update().where(
                    self.metadata.tables['cars'].c.id == car_id
                ).values(**updates).returning(self.metadata.tables['cars'].c.id, self.metadata.tables['cars'].c.brand, self.metadata.tables['cars'].c.model, self.metadata.tables['cars'].c.year, self.metadata.tables['cars'].c.is_available, self.metadata.tables['cars'].c.user_id)
                return self.db.execute_statement(update_stmt)
            except Exception as e:
                print(f"Error updating car: {e}")
                raise
            
        def delete_car(self, car_id):
            try:
                delete_stmt = self.metadata.tables['cars'].delete().where(
                    self.metadata.tables['cars'].c.id == car_id
                )
                self.db.execute_statement(delete_stmt)
                return "Car with id " + str(car_id) + " deleted"
            except Exception as e:
                print(f"Error deleting car: {e}")
                raise