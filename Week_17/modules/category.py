class Category:

    def __init__(self, cat_id, category_name, category_type):
        self.__cat_id = cat_id
        self.__category_name = self.__verify_category_name(category_name)
        self.__category_type = category_type


    def get_category_as_dict(self):
        return {
            "Id": self.__cat_id,
            "Category": self.__category_name,
            "Type": self.__category_type
        }
    

    def get_category_details_as_list(self):
        return [self.__cat_id, self.__category_name, self.__category_type]

    def get_category_name(self):
        return self.__category_name
    

    def get_category_id(self):
        return self.__cat_id
    

    def get_category_type(self):
        return self.__category_type
    
    
    @classmethod
    def expense(cls):
        return cls("Expense")
    

    @classmethod
    def income(cls):
        return cls("Income")
    
    def __verify_category_name(self, name):
        if len(name) > 0:
            return name
        else:
            raise ValueError("Category name cannot be empty.")