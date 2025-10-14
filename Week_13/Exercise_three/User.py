from datetime import datetime


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = (datetime.now() - birth_date).days // 365
        return age