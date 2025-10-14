from User import User

def is_adult(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, User):
                if arg.age < 18:
                    print(f"Error running {func.__name__}: User is not an adult.")
                    return
        return func(*args)
    
    return wrapper


@is_adult
def buy_alcohol(user, item, count):
    print(f"{user.name} bought {count} bottles of {item}.")

@is_adult
def enter_club(user):
    print(f"{user.name} entered the club.")

@is_adult
def rent_car(user, car_model):
    print(f"{user.name} rented a {car_model}.")

@is_adult
def book_hotel(user, hotel_name, nights):
    print(f"{user.name} booked {nights} nights at {hotel_name}.")

def main():
    try:
        user1 = User("Alice", "1990-05-15")
        user2 = User("Bob", "1985-10-30") 
        user3 = User("Charlie", "2015-07-22")  

        buy_alcohol(user1, "Whiskey", 2)
        enter_club(user2)
        rent_car(user1, "Toyota")
        book_hotel(user2, "Hilton", 3)

        buy_alcohol(user3, "Vodka", 1)
        enter_club(user3)
        rent_car(user3, "Honda")
        book_hotel(user3, "Marriott", 2)

    except Exception as ex:
        print(f"Error: {ex}")


main()