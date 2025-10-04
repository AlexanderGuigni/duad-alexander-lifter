
# 1.Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

one_more = True
user_list = []

while one_more:
    user_list.append(input("Type a number to add tot he list: "))
    if input("Do you want to add another number to the list (Y=Yes/N=No): ") != "Y":
        one_more = False
        print(f"This is the list geberated {user_list}")

number_to_search = input("Wich number want to search: ")

counter = 0
for item in user_list:
    if item == number_to_search:
        counter = counter + 1

print(f"Number {number_to_search} appears {counter} time in the list ")

# 2.Cree un programa que verifique si todos los elementos de una lista son positivos

my_list = [1,2,3,-4,5,6,7,8,9]
#my_list = [1,2,3,0,5,6,7,8,9]
#my_list = [1,2,3,4,5,6,7,8,9]


for index,number in enumerate(my_list):
    if number <= 0:
        print("There is at least one negative number or zero.")
        break
    if index == (len(my_list)-1):
        print("All numbers in the list are positive")

# 3. Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list = [20,35,10,5,98,65,12,20,60,100,6]
min_number = my_list[0]

for number in my_list:
    if number < min_number:
        min_number = number

print(f"The lowest number on the list is {min_number}")

# 4.Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]

average = 0

for number in my_list:
    average = average + number

average =  average / len(my_list)

new_list = []

for number in my_list:
    if number > average:
        new_list.append(number)

print(f"Average: {average}")
print(f"New List: {new_list}")

# 5.Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

word_list = []

for counter in range(5):
    word_list.append(input(f"{counter + 1}-Ty a new word: "))

new_word_list = []
for word in word_list:
    if len(word) > 4:
        new_word_list.append(word)

print(word_list)
print(new_word_list)