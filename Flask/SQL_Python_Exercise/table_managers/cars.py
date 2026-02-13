from enum import Enum


class Cars:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_car(self, body):
        self.validate_not_empty(body.get(CarFields.BRAND.value), CarFields.BRAND.value)
        self.validate_not_empty(body.get(CarFields.MODEL.value), CarFields.MODEL.value)
        self.validate_year(body.get(CarFields.YEAR.value))
        if body.get(CarFields.IS_AVAILABLE.value) is None:
            body[CarFields.IS_AVAILABLE.value] = True
        else:
            self.validate_boolean(body.get(CarFields.IS_AVAILABLE.value), CarFields.IS_AVAILABLE.value)

        self.db_connection.execute_query(
            "INSERT INTO lifter.cars (brand, model, year, is_available) VALUES (%s, %s, %s, %s)",body[CarFields.BRAND.value], body[CarFields.MODEL.value], body[CarFields.YEAR.value], body[CarFields.IS_AVAILABLE.value]
        )

        return self.get_last_car()
    
    def update_car_availability(self, body):
        self.validate_not_empty(body.get(CarFields.ID.value), CarFields.ID.value)
        self.validate_not_empty(body.get(CarFields.IS_AVAILABLE.value), CarFields.IS_AVAILABLE.value)
        self.validate_car_exists(body.get(CarFields.ID.value))
        is_available = body.get(CarFields.IS_AVAILABLE.value)
        car_id = body.get(CarFields.ID.value)
        self.validate_boolean(is_available, CarFields.IS_AVAILABLE.value)
        self.db_connection.execute_query(
            "UPDATE lifter.cars SET is_available = %s WHERE car_id = %s", is_available, car_id
        )

        return self.get_cars(**{CarFields.ID.value: car_id})
    
    def get_cars(self, **kwargs):
        filters = ""
        for key,value in kwargs.items():
            if filters == "":
                filters = key + "= %s"
            else:
                filters += " AND " + key + "= %s"
        if filters != "":
            filters = " WHERE " + filters
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars" + filters, *list(kwargs.values())
        )
        cars = []
        if results:
            for row in results:
                car = {
                    CarFields.ID.value: row[0],
                    CarFields.BRAND.value: row[1],
                    CarFields.MODEL.value: row[2],
                    CarFields.YEAR.value: row[3],
                    CarFields.IS_AVAILABLE.value: row[4],
                }
                cars.append(car)
        return cars
 
    
    def get_last_car(self):
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars ORDER BY car_id DESC LIMIT 1"
        )
        if results:
            row = results[0]
            car = {
                CarFields.ID.value: row[0],
                CarFields.BRAND.value: row[1],
                CarFields.MODEL.value: row[2],
                CarFields.YEAR.value: row[3],
                CarFields.IS_AVAILABLE.value: row[4],
            }
            return car
        return None
        
    def validate_year(self, year):
        self.validate_not_empty(str(year), CarFields.YEAR.value)
        if len(str(year)) != 4:
            raise ValueError("Year must be a 4-digit integer")
        
    def validate_boolean(self, value, field_name):
        if not isinstance(value, bool):
            raise ValueError(f"{field_name} must be a boolean value")
        
    def validate_car_exists(self, car_id):
        result = self.get_cars(**{CarFields.ID.value:car_id})
        if not result:
            raise ValueError(f"Car with id {car_id} does not exist.")
        
    def validate_car_availability(self, car_id):
        result = self.get_cars(**{CarFields.ID.value:car_id})
        if result and result[0][CarFields.IS_AVAILABLE.value] == False:
            raise ValueError(f"Car with id {car_id} is not available for rental.")
        
    def validate_not_empty(self, value, field_name):
        if value is None or not str(value).strip() or value == "" or value == 'None':
            raise ValueError(f"{field_name} must be a non-empty.")
    

class CarFields(Enum):
    ID = "car_id"
    BRAND = "brand"
    MODEL = "model"
    YEAR = "year"
    IS_AVAILABLE = "is_available"