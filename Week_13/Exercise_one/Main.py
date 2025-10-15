def return_parameter(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            print(f"Function '{func.__name__}' called with parameters: args={args}")
        if len(kwargs) > 0:
            print(f"Function '{func.__name__}' called with parameters: kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}") #Printing the result inside the decorator, so not need to print in main
        return result #I return the result of the original function just in case the caller needs it
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
def greet_with_kwargs(**kwargs):
    name = kwargs.get("name")
    last_name = kwargs.get("last_name")
    return f"Hello, {name} {last_name}!"

@return_parameter
def calculate_total_expenses(*expenses):
    return sum(expenses)


def main():
    try:
        greet_with_kwargs(name="John", last_name="Doe")
        add(5, 3)
        multiply(4, 2)
        greet("John", "Doe")
        calculate_total_expenses(100, 200, 50, 25)
    except Exception as ex:
        print(f"An error occurred: {ex}")

main()