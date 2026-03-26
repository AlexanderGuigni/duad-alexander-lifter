import sqlalchemy
from sqlalchemy import Column, Integer, MetaData, String, DateTime, Boolean
from connection import DatabaseConnection  

metadata_obj = MetaData()

def create_tables(dbEngine):
    user_table = sqlalchemy.Table(
            'users',
            metadata_obj,
            Column('id', Integer, primary_key=True),
            Column('username', String(50), unique=True, nullable=False),
            Column('email', String(120), unique=True, nullable=False),
            Column('created_at', DateTime, nullable=False),
            Column('is_active', Boolean, default=True)
        )

    address_table = sqlalchemy.Table(
            'addresses',
            metadata_obj,
            Column('id', Integer, primary_key=True),
            Column('user_id', Integer, nullable=False),
            Column('address_line', String(200), nullable=False),
            Column('city', String(50), nullable=False),
            Column('state', String(50), nullable=False),
            Column('zip_code', String(10), nullable=False)
        )

    car_table = sqlalchemy.Table(
            'cars',
            metadata_obj,
            Column('id', Integer, primary_key=True),
            Column('user_id', Integer, nullable=True),
            Column('brand', String(50), nullable=False),
            Column('model', String(50), nullable=False),
            Column('year', Integer, nullable=False),
            Column('is_available', Boolean, default=True)
        )

    metadata_obj.create_all(dbEngine)

def insert_initial_data(db_connection):
    initial_users = [
        {"username": "Alice", "email": "alice@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Bob", "email": "bob@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Charlie", "email": "charlie@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "David", "email": "david@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Eve", "email": "eve@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Frank", "email": "frank@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Grace", "email": "grace@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Heidi", "email": "heidi@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Ivan", "email": "ivan@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Judy", "email": "judy@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Karl", "email": "karl@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Leo", "email": "leo@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Mallory", "email": "mallory@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Nina", "email": "nina@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Oscar", "email": "oscar@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Peggy", "email": "peggy@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Quentin", "email": "quentin@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Rupert", "email": "rupert@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Sybil", "email": "sybil@example.com", "created_at": "2024-06-01 00:00:00"},
        {"username": "Trent", "email": "trent@example.com", "created_at": "2024-06-01 00:00:00"}
    ]
    
    insert_users_stmt = metadata_obj.tables['users'].insert().values(initial_users)

    initial_addresses = [
        {"user_id": 1, "address_line": "123 Maple St", "city": "Springfield", "state": "IL", "zip_code": "62701"},
        {"user_id": 2, "address_line": "456 Oak Ave", "city": "Madison", "state": "WI", "zip_code": "53703"},
        {"user_id": 3, "address_line": "789 Pine Rd", "city": "Austin", "state": "TX", "zip_code": "73301"},
        {"user_id": 4, "address_line": "101 Cedar Ln", "city": "Miami", "state": "FL", "zip_code": "33101"},
        {"user_id": 5, "address_line": "202 Elm Blvd", "city": "Seattle", "state": "WA", "zip_code": "98101"},
        {"user_id": 6, "address_line": "303 Birch St", "city": "Denver", "state": "CO", "zip_code": "80201"},
        {"user_id": 7, "address_line": "404 Walnut Ave", "city": "Phoenix", "state": "AZ", "zip_code": "85001"},
        {"user_id": 8, "address_line": "505 Cherry Rd", "city": "Boston", "state": "MA", "zip_code": "02108"},
        {"user_id": 9, "address_line": "606 Aspen Dr", "city": "Portland", "state": "OR", "zip_code": "97201"},
        {"user_id": 10, "address_line": "707 Willow Way", "city": "Atlanta", "state": "GA", "zip_code": "30301"},
        {"user_id": 11, "address_line": "808 Poplar Ct", "city": "Nashville", "state": "TN", "zip_code": "37201"},
        {"user_id": 12, "address_line": "909 Sycamore Pl", "city": "Dallas", "state": "TX", "zip_code": "75201"},
        {"user_id": 13, "address_line": "111 Lakeview St", "city": "San Diego", "state": "CA", "zip_code": "92101"},
        {"user_id": 14, "address_line": "222 Hillcrest Ave", "city": "Charlotte", "state": "NC", "zip_code": "28202"},
        {"user_id": 15, "address_line": "333 River Rd", "city": "Columbus", "state": "OH", "zip_code": "43215"},
        {"user_id": 16, "address_line": "444 Sunset Blvd", "city": "Las Vegas", "state": "NV", "zip_code": "88901"},
        {"user_id": 17, "address_line": "555 Meadow Ln", "city": "Boise", "state": "ID", "zip_code": "83702"},
        {"user_id": 18, "address_line": "666 Forest Dr", "city": "Burlington", "state": "VT", "zip_code": "05401"},
        {"user_id": 19, "address_line": "777 Ocean Ave", "city": "Providence", "state": "RI", "zip_code": "02903"},
        {"user_id": 20, "address_line": "888 Highland Rd", "city": "Cheyenne", "state": "WY", "zip_code": "82001"}
    ]

    insert_addresses_stmt = metadata_obj.tables['addresses'].insert().values(initial_addresses)

    initial_cars = [
        {"user_id": 1, "brand": "Toyota", "model": "Corolla", "year": 2018, "is_available": True},
        {"user_id": 2, "brand": "Honda", "model": "Civic", "year": 2019, "is_available": True},
        {"user_id": 3, "brand": "Ford", "model": "Focus", "year": 2017, "is_available": True},
        {"user_id": 4, "brand": "Chevrolet", "model": "Malibu", "year": 2020, "is_available": False},
        {"user_id": 5, "brand": "Nissan", "model": "Sentra", "year": 2021, "is_available": True},
        {"user_id": 6, "brand": "Hyundai", "model": "Elantra", "year": 2018, "is_available": True},
        {"user_id": 7, "brand": "Kia", "model": "Forte", "year": 2022, "is_available": False},
        {"user_id": 8, "brand": "Volkswagen", "model": "Jetta", "year": 2019, "is_available": True},
        {"user_id": 1, "brand": "Mazda", "model": "3", "year": 2020, "is_available": True},
        {"user_id": 10, "brand": "Subaru", "model": "Impreza", "year": 2017, "is_available": True},
        {"user_id": 11, "brand": "BMW", "model": "320i", "year": 2016, "is_available": False},
        {"user_id": 12, "brand": "Mercedes-Benz", "model": "C200", "year": 2021, "is_available": True},
        {"user_id": 13, "brand": "Audi", "model": "A4", "year": 2018, "is_available": True},
        {"user_id": 13, "brand": "Lexus", "model": "IS", "year": 2020, "is_available": False},
        {"user_id": 13, "brand": "Tesla", "model": "Model 3", "year": 2022, "is_available": True},
        {"user_id": None, "brand": "Renault", "model": "Clio", "year": 2016, "is_available": True},
        {"user_id": None, "brand": "Peugeot", "model": "208", "year": 2019, "is_available": True},
        {"user_id": None, "brand": "Fiat", "model": "Tipo", "year": 2017, "is_available": False},
        {"user_id": None, "brand": "Skoda", "model": "Octavia", "year": 2021, "is_available": True},
        {"user_id": None, "brand": "Seat", "model": "Leon", "year": 2018, "is_available": True}
    ]

    insert_cars_stmt = metadata_obj.tables['cars'].insert().values(initial_cars)

    db_connection.execute_multiple_statements([insert_users_stmt, insert_addresses_stmt, insert_cars_stmt])

class User:

    def __init__(self,db_connection):
        self.db = db_connection
        self.metadata = metadata_obj


    def get_user(self, **filters):
        try:
            select_stmt = self.metadata.tables['users'].select().where(
                sqlalchemy.and_(*[getattr(self.metadata.tables['users'].c, key) == value for key, value in filters.items()])
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        
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
            return None

    def create_user(self, username, email, created_at, is_active=True):
        try:
            insert_stmt = self.metadata.tables['users'].insert().values(
                username=username,
                email=email,
                created_at=created_at,
                is_active=is_active
            ).returning(self.metadata.tables['users'].c.id, self.metadata.tables['users'].c.username, self.metadata.tables['users'].c.email, self.metadata.tables['users'].c.created_at, self.metadata.tables['users'].c.is_active)
            return self.db.execute_statement(insert_stmt)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        
    def update_user(self, user_id, **updates):
        try:
            update_stmt = self.metadata.tables['users'].update().where(
                self.metadata.tables['users'].c.id == user_id
            ).values(**updates).returning(self.metadata.tables['users'].c.id, self.metadata.tables['users'].c.username, self.metadata.tables['users'].c.email, self.metadata.tables['users'].c.created_at, self.metadata.tables['users'].c.is_active)
            return self.db.execute_statement(update_stmt)
        except Exception as e:
            print(f"Error updating user: {e}")
            return None
        
    def delete_user(self, user_id):
        try:
            delete_stmt = self.metadata.tables['users'].delete().where(
                self.metadata.tables['users'].c.id == user_id
            ).returning("User with id " + str(user_id) + " deleted")
            return self.db.execute_statement(delete_stmt)
        except Exception as e:
            print(f"Error deleting user: {e}")
            return None
        
    @property
    def addresses(self,user_id):
        try:
            select_stmt = self.metadata.tables['addresses'].select().where(
                self.metadata.tables['addresses'].c.user_id == user_id
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching addresses for user: {e}")
            return None
        
    @property
    def cars(self,user_id):
        try:
            select_stmt = self.metadata.tables['cars'].select().where(
                self.metadata.tables['cars'].c.user_id == user_id
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching cars for user: {e}")
            return None

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
            return None
        
    def get_addresses_with_string(self, substring):
        try:
            select_stmt = self.metadata.tables['addresses'].select().where(
                self.metadata.tables['addresses'].c.address_line.ilike(f"%{substring}%")
            )
            return self.db.execute_statement(select_stmt)
        except Exception as e:
            print(f"Error fetching addresses with substring '{substring}': {e}")
            return None
        
    def create_address(self, user_id, address):
        try:
            insert_stmt = self.metadata.tables['addresses'].insert().values(
                user_id=user_id,
                address_line=address
            ).returning(self.metadata.tables['addresses'].c.id, self.metadata.tables['addresses'].c.user_id, self.metadata.tables['addresses'].c.address)
            return self.db.execute_statement(insert_stmt)
        except Exception as e:
            print(f"Error creating address: {e}")
            return None
        
    def update_address(self, address_id, **updates):
        try:
            update_stmt = self.metadata.tables['addresses'].update().where(
                self.metadata.tables['addresses'].c.id == address_id
            ).values(**updates).returning(self.metadata.tables['addresses'].c.id, self.metadata.tables['addresses'].c.user_id, self.metadata.tables['addresses'].c.address)
            return self.db.execute_statement(update_stmt)
        except Exception as e:
            print(f"Error updating address: {e}")
            return None
        
    def delete_address(self, address_id):
        try:
            delete_stmt = self.metadata.tables['addresses'].delete().where(
                self.metadata.tables['addresses'].c.id == address_id
            ).returning("Address with id " + str(address_id) + " deleted")
            return self.db.execute_statement(delete_stmt)
        except Exception as e:
            print(f"Error deleting address: {e}")
            return None
        
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
                return None
            
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
                return None
            
        def update_car(self, car_id, **updates):
            try:
                update_stmt = self.metadata.tables['cars'].update().where(
                    self.metadata.tables['cars'].c.id == car_id
                ).values(**updates).returning(self.metadata.tables['cars'].c.id, self.metadata.tables['cars'].c.brand, self.metadata.tables['cars'].c.model, self.metadata.tables['cars'].c.year, self.metadata.tables['cars'].c.is_available, self.metadata.tables['cars'].c.user_id)
                return self.db.execute_statement(update_stmt)
            except Exception as e:
                print(f"Error updating car: {e}")
                return None
            
        def delete_car(self, car_id):
            try:
                delete_stmt = self.metadata.tables['cars'].delete().where(
                    self.metadata.tables['cars'].c.id == car_id
                ).returning("Car with id " + str(car_id) + " deleted")
                return self.db.execute_statement(delete_stmt)
            except Exception as e:
                print(f"Error deleting car: {e}")
                return None