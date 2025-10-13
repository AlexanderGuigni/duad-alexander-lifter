from Car import Car
from Motorcycle import Motorcycle

def main():
    car = Car("Toyota", 2020, 4)
    motorcycle = Motorcycle("Yamaha", 2019, "Sport")

    print(car.get_info())
    print(motorcycle.get_info())

main()