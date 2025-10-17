def is_number(func):
    def wrapper(*args, **kwargs):
        all_args = args + tuple(kwargs.values())
        try:
            if not all(isinstance(arg, (int, float)) for arg in all_args):
                raise TypeError("Error: All parameters must be numbers.")
            result = func(*args, **kwargs)
            print(f"For function '{func.__name__}' with parameters: {all_args}, the result is: {result}")
            return result
        except TypeError as ex:
            print(ex)
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

@is_number
def multiply_kwargs(**kwargs):
    a = kwargs.get('a')
    b = kwargs.get('b')
    return a * b

def main():
    try:
        add(5, 3)
        multiply(4, 2)
        calculate_total_expenses(100, 200, 50, 25)
        add(5, "three")
        multiply_kwargs(a=4, b="two")
        multiply_kwargs(a=4, b=15.5)
        calculate_total_expenses("100", 200, 50, 25)
    except Exception as ex:
        print(f"An error occurred: {ex}")

main()