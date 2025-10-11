from Shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        try:
            return round(3.14 * self.radius ** 2, 2)
        except Exception as ex:
            print(f"Error calculating area: {ex}")

    def calculate_perimeter(self):
        try:
            return round(2 * 3.14 * self.radius, 2)
        except Exception as ex:
            print(f"Error calculating perimeter: {ex}")