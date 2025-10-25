def sum_two_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both parameters must be numeric")
    return a + b


def subtract_two_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both parameters must be numeric")
    return a - b


def multiply_two_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both parameters must be numeric")
    return a * b


def divide_two_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both parameters must be numeric")
    elif b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b