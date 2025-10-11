from BankAccount import BankAccount
from SavingAccount import SavingAccount

def main():
    print("Creating a BankAccount")
    account = BankAccount()

    print("Initial Deposit")
    account.deposit(500)

    print("Withdrawing 300")
    account.withdraw(300)

    print("Withdrawing 300")
    account.withdraw(300)

    print(f"Final Balance: {account.get_balance()}")

    print("\n-----------------------\n")

    print("Creating a SavingAccount with main balance of 200")
    saving_account = SavingAccount(200)

    print("Initial Deposit")
    saving_account.deposit(1000)

    print("Withdrawing 700")
    saving_account.withdraw(700)

    print("Withdrawing 200")
    saving_account.withdraw(200)

    print(f"Final Balance: {saving_account.get_balance()}")

main()