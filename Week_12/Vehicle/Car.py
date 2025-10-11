from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return f"Car: {self.brand} {self.year}, Doors: {self.doors}"