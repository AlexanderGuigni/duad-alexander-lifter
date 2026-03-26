from models import create_tables, insert_initial_data, User, Address, Cars
from connection import DatabaseConnection


if __name__ == "__main__":
    db_connection = DatabaseConnection()
    
    # Create tables if they don't exist
    create_tables(db_connection.engine)

    # Insert initial data
    insert_initial_data(db_connection)

    # Example usage
    user_model = User(db_connection)
    address_model = Address(db_connection)
    cars_model = Cars(db_connection)

    # Create a new user
    new_user = user_model.create_user(username="Samuel Guigni", email="samuel.guigni@example.com", created_at="2024-06-01 00:00:00")
    print("New User:", new_user)

    # Create an address for the new user
    if new_user:   
        user_id = new_user[0][0]
        new_address = address_model.create_address(user_id=user_id, address="123 Main St")
        print("New Address:", new_address)

    # Create a car for the new user
        new_car = cars_model.create_car(brand="Toyota", model="Corolla", year=2020)
        print("New Car:", new_car)

    # Associate the car with the user
        if new_car:
            car_id = new_car[0][0]
            cars_model.update_car(car_id, user_id=user_id)
            print(f"Car with ID {car_id} associated with User ID {user_id}")

    # Get all users
    users = user_model.get_user()
    print("All Users:", users)

    # Get all addresses
    addresses = address_model.get_address()
    print("All Addresses:", addresses)

    # Get all cars
    cars = cars_model.get_car()
    print("All Cars:", cars)

    # Get cars for a specific user
    user_cars = cars_model.get_car(user_id=user_id)
    print(f"Cars for User ID {user_id}:", user_cars)

    # Get addresses for a specific user
    user_addresses = address_model.get_address(user_id=user_id)
    print(f"Addresses for User ID {user_id}:", user_addresses)

    # Get cars without an associated user
    unassociated_cars = cars_model.get_car(user_id=None)
    print("Cars without an associated user:", unassociated_cars)

    # Get user with more than 1 car
    users_with_multiple_cars = user_model.get_users_with_multiple_cars()
    print("Users with more than 1 car:", users_with_multiple_cars)

    # Get addresses containing a specific substring
    substring = "St"
    addresses_with_substring = address_model.get_addresses_with_string(substring)
    print(f"Addresses containing '{substring}':", addresses_with_substring)

