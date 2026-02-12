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
        self.users_manager.validate_user_exists(body.get(RentalFields.USER_ID.value))
        self.cars_manager.validate_car_exists(body.get(RentalFields.CAR_ID.value))
        self.users_manager.validate_user_is_enabled(body.get(RentalFields.USER_ID.value))
        self.cars_manager.validate_car_availability(body.get(RentalFields.CAR_ID.value))
        if body.get(RentalFields.RENTAL_DATE.value) is None:
            body[RentalFields.RENTAL_DATE.value] = datetime.now().strftime('%Y-%m-%d')
        self.validate_rental_date(body.get(RentalFields.RENTAL_DATE.value))

        self.db_connection.execute_query(
            "INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned) VALUES (%s, %s, %s, %s)",
            body[RentalFields.USER_ID.value], body[RentalFields.CAR_ID.value], body[RentalFields.RENTAL_DATE.value], False
        )

        self.cars_manager.update_car_availability({CarFields.ID.value: body.get(RentalFields.CAR_ID.value), CarFields.IS_AVAILABLE.value: False})

        return self.get_last_rental()
    
    def update_rental_return_status(self, body):
        self.validate_not_empty(body.get(RentalFields.ID.value), RentalFields.ID.value)
        self.validate_not_empty(body.get(RentalFields.IS_RETURNED.value), RentalFields.IS_RETURNED.value)
        self.validate_boolean(body.get(RentalFields.IS_RETURNED.value), RentalFields.IS_RETURNED.value)
        rental = self.validate_rental_exists(body.get(RentalFields.ID.value))
        is_returned = body.get(RentalFields.IS_RETURNED.value)
        rental_id = rental.get(RentalFields.ID.value)
        current_returned_status = rental[RentalFields.IS_RETURNED.value]
        print(current_returned_status, is_returned)
        if current_returned_status == is_returned:
            raise Exception(f"Info: Rental with id {rental_id} already has is_returned set to {is_returned}.")

        self.db_connection.execute_query(
            "UPDATE lifter.rentals SET is_returned = %s WHERE rental_id = %s",
            is_returned, rental_id
        )

        return self.get_rentals(**{RentalFields.ID.value: rental_id})
    
    def return_rental(self, body):
        self.validate_not_empty(body.get(RentalFields.ID.value), RentalFields.ID.value)
        rental = self.validate_rental_exists(body.get(RentalFields.ID.value))
        car_id = rental[RentalFields.CAR_ID.value]
        current_returned_status = rental[RentalFields.IS_RETURNED.value]

        if current_returned_status == True:
            raise Exception(f"Info: Rental with id {body.get(RentalFields.ID.value)} has already been returned.")

        self.db_connection.execute_query(
            "UPDATE lifter.rentals SET is_returned = %s WHERE rental_id = %s",
            True, body.get(RentalFields.ID.value)
        )

        self.cars_manager.update_car_availability({CarFields.ID.value: car_id, CarFields.IS_AVAILABLE.value: True})

        return self.get_rentals(**{RentalFields.ID.value: body.get(RentalFields.ID.value)})
        
    
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
            
    def get_rentals(self, **kwargs):
        filters = ""
        for key,value in kwargs.items():
            if filters == "":
                filters = key + "= %s"
            else:
                filters += " AND " + key + "= %s"
        if filters != "":
            filters = " WHERE " + filters
        results = self.db_connection.execute_query(
            "SELECT rental_id, user_id, car_id, rental_date, is_returned FROM lifter.rentals" + filters, *list(kwargs.values())
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
        
    def validate_boolean(self, value, field_name):
        if not isinstance(value, bool):
            raise ValueError(f"{field_name} must be a boolean value")
        
    def validate_rental_date(self, rental_date):
        if not rental_date or not rental_date.strip():
                raise ValueError(f"Rental date cannot be empty")
        try:
            datetime.strptime(rental_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Rental date must be in YYYY-MM-DD format")
    
    def validate_not_empty(self, value, field_name):
        if value is None or not str(value).strip() or value == "" or value == 'None':
            raise ValueError(f"{field_name} must be a non-empty.")
    
    def validate_rental_exists(self, rental_id):
        result = self.get_rentals(**{RentalFields.ID.value:rental_id})
        if not result:
            raise ValueError(f"Rental with id {rental_id} does not exist.")
        else:
            return result[0]
        
        
    
        
class RentalFields(Enum):
    ID = "rental_id"
    USER_ID = "user_id"
    CAR_ID = "car_id"
    RENTAL_DATE = "rental_date"
    IS_RETURNED = "is_returned"