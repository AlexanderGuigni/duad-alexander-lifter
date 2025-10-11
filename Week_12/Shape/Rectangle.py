from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        try:
            return round(self.width * self.height, 2)
        except Exception as ex:
            print(f"Error calculating area: {ex}")

    def calculate_perimeter(self):
        try:
            return round(2 * (self.width + self.height), 2)
        except Exception as ex:
            print(f"Error calculating perimeter: {ex}")