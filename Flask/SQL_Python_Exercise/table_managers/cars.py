from enum import Enum


class Cars:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_car(self, body):
        self.validate_not_empty(body.get(CarFields.BRAND.value), CarFields.BRAND.value)
        self.validate_not_empty(body.get(CarFields.MODEL.value), CarFields.MODEL.value)
        self.validate_year(body.get(CarFields.YEAR.value))
        self.validate_one_or_cero(int(body.get(CarFields.IS_AVAILABLE.value)), CarFields.IS_AVAILABLE.value)

        self.db_connection.execute_query(
            "INSERT INTO lifter.cars (brand, model, year, is_available) VALUES (%s, %s, %s, %s)",body[CarFields.BRAND.value], body[CarFields.MODEL.value], body[CarFields.YEAR.value], int(body[CarFields.IS_AVAILABLE.value])
        )

        return self.get_last_car()
    
    def update_car_availability(self, car_id, is_available):
        is_available = int(is_available)
        self.validate_one_or_cero(is_available, CarFields.IS_AVAILABLE.value)
        self.db_connection.execute_query(
            "UPDATE lifter.cars SET is_available = %s WHERE car_id = %s", is_available, car_id
        )

        return self.get_car_by_id(car_id)
    
    def get_all_cars(self):
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars"
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
    
    def get_car_by_id(self, car_id):
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars WHERE car_id = %s", car_id
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

    def get_cars_by_availability(self, is_available):
        is_available = int(is_available)
        self.validate_one_or_cero(is_available, CarFields.IS_AVAILABLE.value)
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars WHERE is_available = %s", is_available
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
    
    def get_cars_by_model(self, model):
        self.validate_not_empty(model, CarFields.MODEL.value)
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars WHERE model = %s", model
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
    
    def get_cars_by_brand(self, brand):
        self.validate_not_empty(brand, CarFields.BRAND.value)
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars WHERE brand = %s", brand
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
    
    def get_cars_by_year(self, year):
        year = int(year)
        self.validate_year(year)
        results = self.db_connection.execute_query(
            "SELECT car_id, brand, model, year, is_available FROM lifter.cars WHERE year = %s", year
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

    def validate_not_empty(self, value, field_name):
        if not value or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty.")
        
    def validate_year(self, year):
        self.validate_not_empty(str(year), CarFields.YEAR.value)
        if len(str(year)) != 4:
            raise ValueError("Year must be a 4-digit integer")
        
    def validate_one_or_cero(self, value, field_name):
        if int(value) not in [0, 1]:
            raise ValueError(f"{field_name} must be 1 = TRUE or 0 = FALSE")
        

class CarFields(Enum):
    ID = "car_id"
    BRAND = "brand"
    MODEL = "model"
    YEAR = "year"
    IS_AVAILABLE = "is_available"