# 1.Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_first_half_of_the_text():
    print("I love.. ")


def print_complte_text():
    print_first_half_of_the_text()
    print("programming")


print_complte_text()

# 2. Experimente con el concepto de scope:
    # 1. Intente accesar a una variable definida dentro de una función desde afuera.

def print_love_programing_text():
    love_text = "I love..."
    print(f"{love_text} programming")


print_complte_text()
# Error -> print(love_text)

    #2.  Intente accesar a una variable global desde una función y cambiar su valor.

love_text_two = "I love..."


def print_love_programing_text():
    love_text_two = "I really love"
    print(f"{love_text_two} programming")


print_love_programing_text()
print(love_text_two)

def print_love_programing_text_two():
    global love_text_two
    love_text_two = "I really really love"
    print(f"{love_text_two} programming")

print_love_programing_text_two()
print(love_text_two)

# 3. Cree una función que retorne la suma de todos los números de una lista.
    # 1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    # 2. [4, 6, 2, 29] → 41

def sum_numbers_in_list(number_list):
    total = 0
    for element in number_list:
        total = total + element
    return total


def main():
    number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(f"The total is {sum_numbers_in_list(number_list)}")


main()

# 4. Cree una función que le de la vuelta a un string y lo retorne.

def invert_string(my_string):
    string_len = len(my_string)
    inverted_string = ""

    for index in range(string_len):
        inverted_string = inverted_string + my_string[(string_len-1)-index]
    
    return inverted_string


def main():
    my_string = input("Type any word or phrase: ")
    print(f"This is the same phase but inverted: {invert_string(my_string)}")


main()

# 5.Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_lower_upper_letters(my_string):
    upper_total = 0
    lower_total = 0

    for letter in my_string:
        if letter.isalpha():
            if letter.isupper():
                upper_total = upper_total + 1
            elif letter.lower():
                lower_total = lower_total + 1
        
    return f"There’s {upper_total} upper cases and {lower_total} lower cases"


def main():
    my_string = input("Type any word or phrase: ")
    print(count_lower_upper_letters(my_string))


main()

# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    #1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    #2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_string_with_words_separated_by_dash_alphabetically (string_of_words_separated_by_dash):
    words_list_alphabetically_sorted = string_of_words_separated_by_dash.split("-")

    words_list_alphabetically_sorted.sort()

    string_of_words_separated_by_dash_alphabetically_sorted = ""
    
    for index,word in enumerate(words_list_alphabetically_sorted):

        if index != 0 & index != len(words_list_alphabetically_sorted)-1:
            string_of_words_separated_by_dash_alphabetically_sorted = string_of_words_separated_by_dash_alphabetically_sorted + "-"
        
        string_of_words_separated_by_dash_alphabetically_sorted = string_of_words_separated_by_dash_alphabetically_sorted + word

    return string_of_words_separated_by_dash_alphabetically_sorted


def main():
    my_string = "python-variable-funcion-computadora-monitor"

    print(sort_string_with_words_separated_by_dash_alphabetically(my_string))


main()

# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    #1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    #2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    #3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def is_prime_number(number):
    if number >= 2:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for counter in range(2,number):
                if number % (counter + 1) == 0:
                    return False
                return True
    else:
        return False


def remove_composite_numbers(number_list):
    prime_numbers_list = []
    for number in number_list:
        if is_prime_number(number):
            prime_numbers_list.append(number)
    return prime_numbers_list


def main():
    number_list = [1, 4, 6, 7, 13, 9, 67, 0, -1, 97]
    print(remove_composite_numbers(number_list))


main()
