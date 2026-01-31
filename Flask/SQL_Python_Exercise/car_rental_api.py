from flask import Flask, request
from postgre_sql.sql_connection import DatabaseConnection
from table_managers.users import Users, UserFields
from table_managers.cars import Cars, CarFields
from table_managers.rentals import Rentals, RentalFields

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Car Rental API!"

@app.route("/user", methods=["POST"])
def create_user():
    try:
        connection = DatabaseConnection()
        users_manager = Users(connection)
        user_created = users_manager.create_user(request.json)
        return {"message": "User created successfully.", "user": user_created}, 201
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
@app.route("/car", methods=["POST"])
def add_car():
    try:
        connection = DatabaseConnection()
        cars_manager = Cars(connection)
        car_created = cars_manager.create_car(request.json)
        return {"message": "Car added successfully.", "car": car_created}, 201
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

@app.route("/rental", methods=["POST"])
def create_rental():
    try:
        connection = DatabaseConnection()
        rentals_manager = Rentals(connection)
        rental = rentals_manager.create_rental(request.json)
        return {"message": "Rental created successfully.", "rental": rental}, 201
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
@app.route("/car/<car_id>/enable/<is_available>", methods=["PUT"])
def update_car_status(car_id, is_available):
    try:
        connection = DatabaseConnection()
        cars_manager = Cars(connection)
        car_updated = cars_manager.update_car_availability(car_id, is_available)
        return {"message": "Car status updated successfully.", "car": car_updated}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

@app.route("/rental/<rental_id>/return/<is_returned>", methods=["PUT"])
def update_rental_status(rental_id, is_returned):
    try:
        connection = DatabaseConnection()
        rentals_manager = Rentals(connection)
        rental_updated = rentals_manager.update_rental_return_status(rental_id, is_returned)
        return {"message": "Rental updated successfully.", "rental": rental_updated}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
@app.route("/rental/<rental_id>/return", methods=["POST"])
def return_rental(rental_id):
    try:
        connection = DatabaseConnection()
        rentals_manager = Rentals(connection)
        rental_returned = rentals_manager.return_rental(rental_id)
        return {"message": "Rental updated successfully.", "rental": rental_returned}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

@app.route("/user/<user_id>/enable/<is_enabled>", methods=["PUT"])
def update_user_status(user_id, is_enabled):
    try:
        connection = DatabaseConnection()
        users_manager = Users(connection)
        user_updated = users_manager.update_user_status(user_id, is_enabled)
        return {"message": "User status updated successfully.", "user": user_updated}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    

@app.route("/user/<user_id>/arrear/<is_in_arrears>", methods=["PUT"])
def update_user_arrear_status(user_id, is_in_arrears):
    try:
        connection = DatabaseConnection()
        users_manager = Users(connection)
        user_updated = users_manager.update_user_arrear_status(user_id, is_in_arrears)
        return {"message": "User arrear status updated successfully.", "user": user_updated}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
@app.route("/users", methods=["GET"])
def get_users():
    try:
        connection = DatabaseConnection()
        users_manager = Users(connection)   
        if request.args.get(UserFields.IS_ENABLED.value):
            users = users_manager.get_users_by_status(request.args.get(UserFields.IS_ENABLED.value))
        elif request.args.get(UserFields.IS_IN_ARREARS.value):
            users = users_manager.get_users_by_arrear_status(request.args.get(UserFields.IS_IN_ARREARS.value))
        elif request.args.get(UserFields.ID.value):
            users = users_manager.get_user_by_id(request.args.get(UserFields.ID.value))
        else:
            users = users_manager.get_all_users()
        
        return {"users": users}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

@app.route("/cars", methods=["GET"])
def get_cars():
    try:
        connection = DatabaseConnection()
        cars_manager = Cars(connection)
        if request.args.get(CarFields.IS_AVAILABLE.value):
            cars = cars_manager.get_cars_by_availability(request.args.get(CarFields.IS_AVAILABLE.value))
            return {"cars": cars}, 200
        elif request.args.get(CarFields.ID.value):
            cars = cars_manager.get_car_by_id(request.args.get(CarFields.ID.value))
            return {"cars": cars}, 200
        elif request.args.get(CarFields.MODEL.value):
            cars = cars_manager.get_cars_by_model(request.args.get(CarFields.MODEL.value))
            return {"cars": cars}, 200
        elif request.args.get(CarFields.BRAND.value):
            cars = cars_manager.get_cars_by_brand(request.args.get(CarFields.BRAND.value))
            return {"cars": cars}, 200
        elif request.args.get(CarFields.YEAR.value):
            cars = cars_manager.get_cars_by_year(request.args.get(CarFields.YEAR.value))
            return {"cars": cars}, 200
        else:
            cars = cars_manager.get_all_cars()
            return {"cars": cars}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
@app.route("/rentals", methods=["GET"])
def get_rentals():
    try:
        connection = DatabaseConnection()
        rentals_manager = Rentals(connection)
        if request.args.get(RentalFields.IS_RETURNED.value):
            rentals = rentals_manager.get_rentals_by_return_status(request.args.get(RentalFields.IS_RETURNED.value))
            return {"rentals": rentals}, 200
        elif request.args.get(RentalFields.USER_ID.value):
            rentals = rentals_manager.get_rentals_by_user_id(request.args.get(RentalFields.USER_ID.value))
            return {"rentals": rentals}, 200
        elif request.args.get(RentalFields.CAR_ID.value):
            rentals = rentals_manager.get_rentals_by_car_id(request.args.get(RentalFields.CAR_ID.value))
            return {"rentals": rentals}, 200
        else:
            rentals = rentals_manager.get_all_rentals()
            return {"rentals": rentals}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500
    
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)