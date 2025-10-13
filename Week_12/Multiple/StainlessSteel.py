from Chromium import Chromium
from Nickel import Nickel
from Molybdenum import Molybdenum
from Manganese import Manganese 
from Iron import Iron
class StainlessSteel(Chromium, Nickel, Molybdenum, Manganese, Iron):

    def show_properties(self):
        print(">> Stainless Steel Properties <<")
        print("")
        print(f"machinability: {self.machinability}")
        print(f"hardness: {self.hardness}")
        print(f"corrosion_resistance: {self.corrosion_resistance}")
        print(f"ductility: {self.ductility}")
        print(f"high_temperature_resistance: {self.high_temperature_resistance}")