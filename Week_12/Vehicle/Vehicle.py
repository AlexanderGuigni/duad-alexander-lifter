class Vehicle:
    def __init__(self, brand,year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"Vehicle:{self.brand} {self.year}"