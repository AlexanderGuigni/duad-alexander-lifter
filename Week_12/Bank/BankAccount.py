class BankAccount:
    balance = 0

    def deposit(self, amount):
        try:
            self.balance += amount
            print(f"Deposited {amount}: Balance {self.balance}")
        except Exception as ex:
            print(f"Error trying to deposit: {ex}")


    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                print(f"Insufficient funds: Balance {self.balance}")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}: Balance {self.balance}")
        except Exception as ex:
            print(f"Error trying to withdraw: {ex}")

    def get_balance(self):
        return self.balance