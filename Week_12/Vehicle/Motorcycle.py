from Vehicle import Vehicle

class Motorcycle(Vehicle):
    
    def __init__(self, brand, year, type_motorcycle):
        super().__init__(brand, year)
        self.type_motorcycle = type_motorcycle

    def get_info(self):
        return f"Motorcycle: {self.brand} {self.year}, Type: {self.type_motorcycle}"