# 1.Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
int_data_type = 8
string_data_type = 'This is a string data type'
bool_data_type = True
float_data_type = 10.52
list_data_type = ['one', 'two', 'three']
tupla_data_type = {1,2,3,4}
dir_data_type = {
    "key_one": 1,
    "key_two": 2
}
int_data_type_2 = 20
string_data_type_2 = ' and this is a another string data type'
bool_data_type_2 = False
float_data_type_2 = 7.123
list_data_type_2 = ['four', 'five', 'six']
tupla_data_type_2 = {5,6,7,8}
dir_data_type_2 = {
    "key_three": 3,
    "key_four": 4
}

print(int_data_type + int_data_type_2)
print(string_data_type + string_data_type_2)
print(bool_data_type + bool_data_type_2)
print(float_data_type + float_data_type_2)
print(list_data_type + list_data_type_2)
#return error print(tupla_data_type + tupla_data_type_2)
#return error print(dir_data_type + dir_data_type_2)

#return error print(int_data_type + string_data_type_2)
#return error print(bool_data_type + string_data_type_2)
#return error print(float_data_type + string_data_type_2)
#return error print(list_data_type + string_data_type_2)

print(int_data_type + float_data_type_2)
print(bool_data_type + int_data_type_2)

# 2.Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("What is your name? ")
last_name = input("What is your last name? ")
years_old = int(input("What old are you? "))

if (years_old < 6):
    print(f'{name} {last_name} is a baby')
elif (years_old < 12):
    print(f'{name} {last_name} is a kid')
elif (years_old < 20):
    print(f'{name} {last_name} is a teenager')
elif (years_old < 25):
    print(f'{name} {last_name} is a young adult')
elif (years_old < 65):
    print(f'{name} {last_name} is an adult')
else:
    print(f'{name} {last_name} is an elderly person')

# 3.Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
import random

secret_number = random.randint(1,10)
print(secret_number)

while (int(input("Type a number: ")) != secret_number):
    print("Incorrect number, try again...")

print("Congratulations, you guessed the secret number!")

# 4.Cree un programa que le pida tres números al usuario y muestre el mayor.
highest_number = 0

for counter in range(3):
    input_number = int(input(f"{counter+1}-Type an number: "))
    if (input_number > highest_number):
            highest_number = input_number

print(f"The highest number entered is: {highest_number}")

'''
5.Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
'''
grade_total = int(input("Type the total of grades you want to evaluate: "))

approved_total = 0
disapproved_total = 0
approved_average = 0.0
disapproved_average = 0.0

for counter in range(grade_total):
    grade = int(input(f"Type the grade #{counter + 1}: "))

    if(grade < 70):
        disapproved_total = disapproved_total + 1
        disapproved_average = disapproved_average + grade
    else:
        approved_total = approved_total + 1
        approved_average = approved_average + grade

if (disapproved_total == 0):
    disapproved_total = 1

if (approved_total == 0):
    approved_total = 1    

total_average = (disapproved_average + approved_average) / grade_total
disapproved_average = disapproved_average / disapproved_total
approved_average = approved_average / approved_total

print(f"All grades (average)= {total_average}")
print(f"Disapproved grades (average)= {disapproved_average}")
print(f"Approved grades (average)= {approved_average}")

