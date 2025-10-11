from Circle import Circle

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        area = circle.get_area()
        print(f"The area of the circle with radius {radius} is {area}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

main()