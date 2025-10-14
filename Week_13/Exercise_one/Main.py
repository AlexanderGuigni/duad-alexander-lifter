def return_parameter(func):
    def wrapper(*args):
        print(f"Function '{func.__name__}' called with parameters: args={args}")
        return func(*args)
    return wrapper

@return_parameter
def add(a, b):
    return a + b

@return_parameter
def multiply(a, b):
    return a * b

@return_parameter
def greet(name, last_name):
    return f"Hello, {name} {last_name}!"

@return_parameter
def calculate_total_expenses(*expenses):
    return sum(expenses)


def main():
    try:
        print(add(5, 3))
        print(multiply(4, 2))
        print(greet("John", "Doe"))
        print(calculate_total_expenses(100, 200, 50, 25))
    except Exception as ex:
        print(f"An error occurred: {ex}")

main()