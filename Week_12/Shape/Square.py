from Shape import Shape

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        try:
            return round(self.side_length ** 2, 2)
        except Exception as ex:
            print(f"Error calculating area: {ex}")

    def calculate_perimeter(self):
        try:
            return round(4 * self.side_length, 2)
        except Exception as ex:
            print(f"Error calculating perimeter: {ex}")