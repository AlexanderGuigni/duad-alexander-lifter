def receive_number_for_operation():
    try:
        number = input("Enter number: ")
        if number.isnumeric():
            return int(number)
        else:
            raise ValueError("The value entered is not a number")
    except ValueError as ex:
        print(f"Error {ex}")
        return receive_number_for_operation()

def receive_operator():
    operator = 0
    try:
        operator = input("Enter the operator (+, -, /, x): ")
        if operator == '+' or operator == "-" or operator == "/" or operator == "x":
            return operator
        else:
            raise ValueError("The operaator is not valid")
    except ValueError as ex:
        print(f"Error {ex}")
        return receive_operator()

def print_operation_result(first_number, operator, second_number):
    result = 0
    try:
        if operator == '+':
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "/":
            result = first_number / second_number
        elif operator == "x":
            result = first_number * second_number
        else:
            raise ValueError("Invalid option")
        
        print(f"The result of the opration {first_number} {operator} {second_number} is: {result}")
        return result
    except ValueError as ex:
        print(f"Error: {ex}")

def validate_if_want_to_continue():
    decision = ""
    try:
        decision = input("Finish (F) or Continue (C)?")
        if decision.upper() == 'F' or decision.upper() == "FINISH":
            return False
        elif  decision.upper() == "C" or decision.upper() == "CONTINUE":
            return True
        else:
            raise ValueError("Invalid option")
    except ValueError as ex:
        print(f"Error {ex}")
        return validate_if_want_to_continue()


def main():
    current_value = 0
    operator = ""
    continue_option = True
    
    try:    
        while continue_option:
            if operator == "":
                current_value = receive_number_for_operation()
            
            operator = receive_operator()

            current_value = print_operation_result(current_value, operator, receive_number_for_operation())

            continue_option = validate_if_want_to_continue()
    except Exception as ex:
        print(f"Error: {ex}")

main()
