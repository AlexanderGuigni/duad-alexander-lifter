class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        try:
            radius = float(self.radius)
            return 3.14 * (radius ** 2)
        except ValueError as ex:
            print(f"Error calculating area: {ex}")
        
