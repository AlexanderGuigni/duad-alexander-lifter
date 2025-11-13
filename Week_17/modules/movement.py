from actions import convert_string_to_date, format_to_money
from datetime import date


class Movement:

    def __init__(self, movement_id, category, description, amount, date, validate_date=True):
        self.__movement_id = movement_id
        self.__category_name = category.get_category_name()
        self.__category_type = category.get_category_type()
        self.__description = self.__validate_description(description)
        self.__amount = self.__validate_amount(amount)
        if validate_date:   
            self.__date = self.__validate_date(date)
        else:
            self.__date = date


    def get_movement_details_as_list(self):
        return [self.__movement_id, self.__category_name, self.__category_type, self.__description, format_to_money(self.__amount, "₡"), self.__date]
    
    def get_movement_as_dict(self):
        return {
            "Id": self.__movement_id,
            "Category": self.__category_name,
            "Type": self.__category_type,
            "Description": self.__description,
            "Amount": self.__amount,
            "Date": self.__date
        }
    def get_movement_amount(self):
        return self.__amount    
    
    def get_movement_date(self):
        return self.__date
    
    def get_movement_category(self):
        return [self.__category_name, self.__category_type] 
    

    def get_movement_id(self):
        return self.__movement_id


    def __validate_amount(self, amount):
        if float(amount) > 0:
            return amount
        else:
            raise ValueError("Amount must be greater than zero.")

    
    def __validate_date(self, date_string):
        date_date = convert_string_to_date(date_string)
        today_date = date.today()
        if date_date > today_date: 
            raise ValueError("Date must be today or in the past.")
        else:
            return date_string


    def __validate_description(self, description):
        if description.strip() != "":
            return description
        else:
            raise ValueError("Description cannot be empty.")