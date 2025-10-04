
'''
1. Cree un programa que:
- Pida al usuario su **nombre**
    - Si el nombre es numérico (`isdigit()`), **haga `raise ValueError("El nombre no puede ser un número")`**

- Luego pida su edad
    - Si no es un número válido, capture el `ValueError` y muestre un mensaje

- Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
'''

def receive_name():
    try:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        else:
            raise ValueError("The name cant be a number")
    except ValueError as ex:
        print(f"Error: {ex}")
    
def receive_age():
    try:
        age = input("Enter your age: ")
        if age.isnumeric():
            return int(age)
        else:
            raise ValueError("The age entered is not a number")
    except ValueError as ex:
        print(f"Error: {ex}")

def main_one():
    name_receved = None
    age_received = None
    try:
        name_receved = receive_name()

        if name_receved!= None:
            age_received = receive_age()
            if age_received != None:
                print(f"Hi {name_receved}!, your age is {age_received}")

    except Exception as ex:
        print(f"Error: {ex}")


main_one()

'''
2. Cree una función `convertir_a_entero(lista)` que:
- Reciba una lista de strings
- Intente convertir cada elemento a entero usando `int()`
- Use `try-except` para atrapar los errores `ValueError`
- Si algún elemento no puede convertirse, mostrar `"No se pudo convertir el elemento: <valor>"` y continuar con los demás
'''

def convert_to_integer(my_list):
    for item in my_list:
        try:
            print(f"\"{item}\" converted to: {int(item)}")
        except ValueError:
            print(f"Could not convert the item: {item}")    


def main_two():
    string_list = ['4', 'hola', '10', '5.2']
    try:
        convert_to_integer(string_list)
    except Exception as ex:
        print(f"Error: {ex}")

main_two()

'''
3. Cree una función `sumar_valores(lista)` que:
- Reciba una lista de elementos (strings, enteros, flotantes mezclados)
- Intente convertir cada elemento a tipo `float`
- Si puede, sume el valor y muestre: `"<valor> sumado correctamente"`
- Si no puede, muestre: `"Elemento inválido: <valor>"`
- Al final, imprima la suma total
'''
def sum_values(my_list):
    sum_total = 0
    for item in my_list:
        try:
            sum_total = sum_total + float(item)
            print(f"Added number: {item}")
        except ValueError as ex:
            print(f"Invalid element: {item}")
    
    return sum_total

def main_three():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    try:
        print(f"Total is: {sum_values(my_list)}")
    except Exception as ex:
        print(f"Error: {ex}")

main_three()