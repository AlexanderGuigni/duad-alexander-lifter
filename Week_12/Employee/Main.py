from Employee import Employee

def main():
    try:
        emp1 = Employee("Alice", 50000)
        emp2 = Employee("Bob", 60000)

        print(f"Employee 1: {emp1.get_name()}, Salary: {emp1.get_salary()}")
        print(f"Employee 2: {emp2.get_name()}, Salary: {emp2.get_salary()}")

        emp1.promote(float(input("Enter promotion percentage for Alice: ")))
        emp2.promote(float(input("Enter promotion percentage for Bob: ")))
    except Exception as ex:
        print("Error:", ex)

main()