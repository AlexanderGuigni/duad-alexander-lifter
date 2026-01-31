from enum import Enum
from datetime import datetime
from .cars import Cars, CarFields
from .users import Users, UserFields

class Rentals:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cars_manager = Cars(db_connection)
        self.users_manager = Users(db_connection)

    def create_rental(self, body):
        self.validate_user_exists(body.get(RentalFields.USER_ID.value))
        self.validate_car_exists(body.get(RentalFields.CAR_ID.value))
        self.validate_user_is_enabled(body.get(RentalFields.USER_ID.value))
        self.validate_car_availability(body.get(RentalFields.CAR_ID.value))
        self.validate_rental_date(body.get(RentalFields.RENTAL_DATE.value))

        self.db_connection.execute_query(
            "INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned) VALUES (%s, %s, %s, %s)",
            body[RentalFields.USER_ID.value], body[RentalFields.CAR_ID.value], body[RentalFields.RENTAL_DATE.value], 0
        )

        self.cars_manager.update_car_availability(body.get(RentalFields.CAR_ID.value), 0)

        return self.get_last_rental()
    
    def update_rental_return_status(self, rental_id, is_returned):
        rental = self.get_rental_by_id(rental_id)
        car_id = rental[RentalFields.CAR_ID.value]
        current_returned_status = rental[RentalFields.IS_RETURNED.value]

        if current_returned_status == is_returned:
            raise ValueError(f"Rental with id {rental_id} already has is_returned set to {is_returned}.")

        self.db_connection.execute_query(
            "UPDATE rentals SET is_returned = %s WHERE id = %s",
            is_returned, rental_id
        )

        return self.get_rental_by_id(rental_id)
    
    def return_rental(self, rental_id):
        rental = self.get_rental_by_id(rental_id)
        car_id = rental[RentalFields.CAR_ID.value]
        current_returned_status = rental[RentalFields.IS_RETURNED.value]

        if current_returned_status:
            raise ValueError(f"Rental with id {rental_id} has already been returned.")

        self.db_connection.execute_query(
            "UPDATE lifter.rentals SET is_returned = %s WHERE rental_id = %s",
            1, rental_id
        )

        self.cars_manager.update_car_availability(car_id, 1)

        return self.get_rental_by_id(rental_id)
        
    
    def get_last_rental(self):
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals ORDER BY rental_id DESC LIMIT 1"
        )
        if results:
            row = results[0]
            rental = {
                RentalFields.ID.value: row[0],
                RentalFields.USER_ID.value: row[1],
                RentalFields.CAR_ID.value: row[2],
                RentalFields.RENTAL_DATE.value: row[3],
                RentalFields.IS_RETURNED.value: row[4],
            }
            return rental
        return None
    
    def get_rental_by_id(self, rental_id):
            result = self.db_connection.execute_query(
                "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals WHERE rental_id = %s",
                rental_id
            )
            if result:
                row = result[0]
                rental = {
                RentalFields.ID.value: row[0],
                RentalFields.USER_ID.value: row[1],
                RentalFields.CAR_ID.value: row[2],
                RentalFields.RENTAL_DATE.value: row[3],
                RentalFields.IS_RETURNED.value: row[4],
            }
                return rental
            else:
                raise ValueError(f"Rental with id {rental_id} does not exist.")
            
    def get_all_rentals(self):
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals"
        )
        rentals = []
        if results:
            for row in results:
                rental = {
                    RentalFields.ID.value: row[0],
                    RentalFields.USER_ID.value: row[1],
                    RentalFields.CAR_ID.value: row[2],
                    RentalFields.RENTAL_DATE.value: row[3],
                    RentalFields.IS_RETURNED.value: row[4],
                }
                rentals.append(rental)
        return rentals
    
    def get_rentals_by_user_id(self, user_id):
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals WHERE user_id = %s",
            user_id
        )
        rentals = []
        if results:
            for row in results:
                rental = {
                    RentalFields.ID.value: row[0],
                    RentalFields.USER_ID.value: row[1],
                    RentalFields.CAR_ID.value: row[2],
                    RentalFields.RENTAL_DATE.value: row[3],
                    RentalFields.IS_RETURNED.value: row[4],
                }
                rentals.append(rental)
        return rentals
    
    def get_rentals_by_car_id(self, car_id):
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals WHERE car_id = %s",
            car_id
        )
        rentals = []
        if results:
            for row in results:
                rental = {
                    RentalFields.ID.value: row[0],
                    RentalFields.USER_ID.value: row[1],
                    RentalFields.CAR_ID.value: row[2],
                    RentalFields.RENTAL_DATE.value: row[3],
                    RentalFields.IS_RETURNED.value: row[4],
                }
                rentals.append(rental)
        return rentals
    
    def get_rentals_by_return_status(self, is_returned):
        is_returned = int(is_returned)
        self.validate_one_or_cero(is_returned, RentalFields.IS_RETURNED.value)
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals WHERE is_returned = %s",
            is_returned
        )
        rentals = []
        if results:
            for row in results:
                rental = {
                    RentalFields.ID.value: row[0],
                    RentalFields.USER_ID.value: row[1],
                    RentalFields.CAR_ID.value: row[2],
                    RentalFields.RENTAL_DATE.value: row[3],
                    RentalFields.IS_RETURNED.value: row[4],
                }
                rentals.append(rental)
        return rentals

    def validate_user_exists(self, user_id):
        result = self.users_manager.get_user_by_id(user_id)
        if not result:
            raise ValueError(f"User with id {user_id} does not exist.") 

    def validate_car_exists(self, car_id):
        result = self.cars_manager.get_car_by_id(car_id)
        if not result:
            raise ValueError(f"Car with id {car_id} does not exist.")
        
    def validate_car_availability(self, car_id):
        result = self.cars_manager.get_car_by_id(car_id)
        if result and result[CarFields.IS_AVAILABLE.value] == 0:
            raise ValueError(f"Car with id {car_id} is not available for rental.")
        
    def validate_user_is_enabled(self, user_id):
        result = self.users_manager.get_user_by_id(user_id)
        if result and result[0][UserFields.IS_ENABLED.value] == 0:
            raise ValueError(f"User with id {user_id} is not enabled.")
        
    def validate_one_or_cero(self, value, field_name):
        if int(value) not in [0, 1]:
            raise ValueError(f"{field_name} must be 1 = TRUE or 0 = FALSE")
        
    def validate_rental_date(self, rental_date):
        if not rental_date or not rental_date.strip():
                raise ValueError(f"Rental date cannot be empty")
        try:
            datetime.strptime(rental_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Rental date must be in YYYY-MM-DD format")
        
        
    
        
class RentalFields(Enum):
    ID = "rental_id"
    USER_ID = "user_id"
    CAR_ID = "car_id"
    RENTAL_DATE = "rental_date"
    IS_RETURNED = "is_returned"