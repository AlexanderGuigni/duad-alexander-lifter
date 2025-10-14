def is_number(func):
    def wrapper(*args):
        if all(isinstance(arg, (int, float)) for arg in args):
            return func(*args)
        else:
            return "Error: All parameters must be numbers."
    return wrapper

@is_number
def add(a, b):
    return a + b

@is_number
def multiply(a, b):
    return a * b

@is_number
def calculate_total_expenses(*expenses):
    return sum(expenses)

def main():
    try:
        print(add(5, 3))  # Valid input
        print(multiply(4, 2))  # Valid input
        print(calculate_total_expenses(100, 200, 50, 25))  # Valid input
        print(add(5, "three"))  # Invalid input
        print(multiply(4, "two"))  # Invalid input
        print(calculate_total_expenses("100", 200, 50, 25))  # Invalid input
    except Exception as ex:
        print(f"An error occurred: {ex}")

main()