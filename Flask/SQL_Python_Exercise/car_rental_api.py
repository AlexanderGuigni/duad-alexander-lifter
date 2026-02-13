from flask import Flask, request
from postgre_sql.sql_connection import DatabaseConnection
from table_managers.users import Users
from table_managers.cars import Cars
from table_managers.rentals import Rentals

app = Flask(__name__)

# ============================================================
# ERROR HANDLERS GLOBALES
# ============================================================

@app.errorhandler(ValueError)
def handle_value_error(error):

    return {"error": "Validation error", "details": str(error)}, 400

@app.errorhandler(Exception)
def handle_generic_error(error):
    if error.args and "Info:" in error.args[0]:
        return {"message": error.args[0]}, 200
    elif error.code:
        return {"error": error.description}, error.code
    else:
        return {"error": "An unexpected error occurred", "details": str(error)}, 500

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    return "Welcome to the Car Rental API!"

@app.route("/user", methods=["POST"])
def create_user():
    connection = DatabaseConnection()
    users_manager = Users(connection)
    user_created = users_manager.create_user(request.json)
    return {"message": "User created successfully.", "user": user_created}, 201
    
@app.route("/car", methods=["POST"])
def add_car():
    connection = DatabaseConnection()
    cars_manager = Cars(connection)
    car_created = cars_manager.create_car(request.json)
    return {"message": "Car added successfully.", "car": car_created}, 201

@app.route("/rental", methods=["POST"])
def create_rental():
    connection = DatabaseConnection()
    rentals_manager = Rentals(connection)
    rental = rentals_manager.create_rental(request.json)
    return {"message": "Rental created successfully.", "rental": rental}, 201
    
@app.route("/car/enable", methods=["PUT"])
def update_car_status():
    connection = DatabaseConnection()
    cars_manager = Cars(connection)
    car_updated = cars_manager.update_car_availability(request.json)
    return {"message": "Car status updated successfully.", "car": car_updated}, 200

@app.route("/rental/return", methods=["PUT"])
def update_rental_status():
    connection = DatabaseConnection()
    rentals_manager = Rentals(connection)
    rental_updated = rentals_manager.update_rental_return_status(request.json)
    return {"message": "Rental updated successfully.", "rental": rental_updated}, 200
    
@app.route("/rental/return", methods=["POST"])
def return_rental():

    connection = DatabaseConnection()
    rentals_manager = Rentals(connection)
    rental_returned = rentals_manager.return_rental(request.json)
    return {"message": "Rental updated successfully.", "rental": rental_returned}, 200

@app.route("/user/enable", methods=["PUT"])
def update_user_status():
    connection = DatabaseConnection()
    users_manager = Users(connection)
    user_updated = users_manager.update_user_status(request.json)
    return {"message": "User status updated successfully.", "user": user_updated}, 200
    
@app.route("/user/arrear", methods=["PUT"])
def update_user_arrear_status():
    connection = DatabaseConnection()
    users_manager = Users(connection)
    user_updated = users_manager.update_user_arrear_status(request.json)
    return {"message": "User arrear status updated successfully.", "user": user_updated}, 200
    
@app.route("/users", methods=["GET"])
def get_users():
    connection = DatabaseConnection()
    users_manager = Users(connection)   
    users = users_manager.get_users(**request.args)
    return {"users": users}, 200

@app.route("/cars", methods=["GET"])
def get_cars():
    connection = DatabaseConnection()
    cars_manager = Cars(connection)
    cars = cars_manager.get_cars(**request.args)
    return {"cars": cars}, 200
    
@app.route("/rentals", methods=["GET"])
def get_rentals():
    connection = DatabaseConnection()
    rentals_manager = Rentals(connection)
    rentals = rentals_manager.get_rentals(**request.args)
    return {"rentals": rentals}, 200
    
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)