from data import Data
from datetime import date
from actions import convert_string_to_date
from category import Category
from movement import Movement

class FinanceManager:

    def __init__(self):
        self.data_manager = Data()
        self.movements_headers = ["Id", "Category", "Type", "Description", "Amount", "Date"]

    def get_categories(self):
        categories = self.data_manager.category_data
        formatted_categories = []
        for category in categories:
            new_category = Category(
                category["Id"],
                category["Category"],
                category["Type"]
            )
            formatted_categories.append(new_category)
        headers = ["Id", "Category", "Type"]
        return [headers, formatted_categories]
    

    def get_movements(self):
        movements = self.data_manager.movements_data
        formatted_movements = []
        for movement in movements:
            category = Category(
                movement["Id"],
                movement["Category"],
                movement["Type"]
            )
            new_movement = Movement(
                movement["Id"],
                category,
                movement["Description"],
                movement["Amount"],
                movement["Date"],
                validate_date=False
            )
            formatted_movements.append(new_movement)
        return [self.movements_headers, formatted_movements]


    def add_category(self, category_name, category_type):
        cat_id = self.data_manager.generate_id(False)
        new_category = Category(cat_id, category_name, category_type)
        self.data_manager.add_category(new_category)
        self.data_manager.save_csv(False)


    def add_movement(self, category_name, amount, description, date):
        movement_id = self.data_manager.generate_id()
        category = filter(lambda cat: cat.get_category_name() == category_name, self.get_categories()[1])
        category = list(category)[0]
        new_movement = Movement(
            movement_id,
            category,
            description,
            amount,
            date
        )
        self.data_manager.add_movement(new_movement)
        self.data_manager.save_csv(is_movements=True) 

    def filter_by_date(self, initial_date, final_date):
        if not isinstance(initial_date, date):
            initial_date = convert_string_to_date(initial_date)
        if not isinstance(final_date, date):
            final_date = convert_string_to_date(final_date)
        filtered_movements = list(filter(lambda movement: initial_date <= convert_string_to_date(movement.get_movement_date()) <= final_date, self.get_movements()[1]))
        return filtered_movements
    

    def get_expenses_categories(self):
        all_categories = self.get_categories()[1]
        expense_categories = list(filter(lambda category: category.get_category_type() == "Expense", all_categories))
        return expense_categories
    
    def get_income_categories(self):
        all_categories = self.get_categories()[1]
        income_categories = list(filter(lambda category: category.get_category_type() == "Income", all_categories))
        return income_categories


    @staticmethod
    def convert_to_list_of_lists(data, is_movement=True):
        if is_movement:
            return list(map(lambda x: x.get_movement_details_as_list(), data))
        else:
            return list(map(lambda x: x.get_category_details_as_list(), data))