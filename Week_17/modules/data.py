import csv

class Data:

    __category_file_path = "duad-alexander-lifter/Week_17/data_files/categories.csv"
    __movements_file_path = "duad-alexander-lifter/Week_17/data_files/movements.csv"

    def __init__(self):
        self.category_data = []
        self.read_csv(False)
        self.movements_data = []
        self.read_csv()
    
    
    
    def read_csv(self, is_movements=True):
        data = []
        filepath = self.__movements_file_path if is_movements else self.__category_file_path
        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except Exception as ex:
            print(f"Error reading CSV: {ex}")
        if is_movements:
            self.movements_data = data
        else:
            self.category_data = data


    def save_csv(self, is_movements=True):
        filepath = self.__movements_file_path if is_movements else self.__category_file_path
        data = self.movements_data if is_movements else self.category_data
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                return True
        except Exception as ex:
            print(f"Error saving CSV: {ex}")
            return False


    def add_category(self, category_name, category_type):
        new_category = {"Id": self.__generate_id(self.category_data), "Category": category_name, "Type": category_type}
        self.category_data.append(new_category)


    def add_movement(self, category_name, category_type, amount, description, date):
        new_movement = {"Id": self.__generate_id(self.movements_data), "Category": category_name, "Type": category_type, "Amount": amount, "Description": description, "Date": date}
        self.movements_data.append(new_movement)


    def __generate_id(self, data_list):
        if len(data_list) <= 1:
            return 1
        else:
            last_id = max(int(item['Id']) for item in data_list)
            return str(last_id + 1)