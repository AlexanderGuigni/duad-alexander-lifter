class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
  
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def promote(self, salary_increase_points):
        try:
            self.__salary = round(self.__salary + (self.__salary * salary_increase_points), 2)
            print(f"{self.__name} has been promoted. New salary: {self.__salary}")
        except Exception as ex:
            print(f"Error promoting employee: {ex}")
