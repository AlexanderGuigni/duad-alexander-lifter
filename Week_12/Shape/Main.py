from Circle import Circle
from Square import Square
from Rectangle import Rectangle

def main():
    print("Shape Area and Perimeter Calculator (All values in cm)")
    print("-----------------------------------")
    print("\n1. Circle")
    circle = Circle(float(input("Enter the radius of the circle: ")))
    print("Circle Area:", circle.calculate_area())
    print("Circle Perimeter:", circle.calculate_perimeter())

    print("\n2. Square")
    square = Square(float(input("Enter the side length of the square: ")))
    print("Square Area:", square.calculate_area())
    print("Square Perimeter:", square.calculate_perimeter())

    print("\n3. Rectangle")
    rectangle = Rectangle(float(input("Enter the width of the rectangle: ")), float(input("Enter the height of the rectangle: ")))
    print("Rectangle Area:", rectangle.calculate_area())
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())

main()