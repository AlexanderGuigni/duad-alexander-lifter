from BankAccount import BankAccount

class SavingAccount(BankAccount):

    def __init__(self,main_balance):
        self.main_balance = main_balance

    def withdraw(self, amount):
        try:
            if self.balance - amount < self.main_balance:
                print(f"Insufficient funds: Balance {self.balance}, Available {self.balance - self.main_balance}")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}: Balance {self.balance}, Available {self.balance - self.main_balance}")
        except Exception as ex:
            print(f"Error triying to withdraw: {ex}")
        