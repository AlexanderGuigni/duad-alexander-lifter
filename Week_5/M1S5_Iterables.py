
# 1.Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

list_1 = ["The", "brown", "jumps", "the", "old", "with", "and", "under", "while",  "dreaming"]
list_2 = ["quick", "fox", "over", "lazy",  "dog",  "grace", "speed", "moonlight",  "of", "freedom"]

for index in range(len(list_1)):
    print(f"{index + 1}- {list_1[index]} {list_2[index]}")

# 2.Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = input("Type any word or phrase: ")
string_len = len(my_string)

for index in range(string_len):
    print(my_string[(string_len-1)-index])

# 3.Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = ["table","chair","book","door","window","phone","lamp","clock","pen","backpack"]

my_list.insert(1,my_list[len(my_list)-1])
my_list.insert(len(my_list)-1, my_list[0])
my_list.pop(0)
my_list.pop(len(my_list)-1)

print(my_list)

# 4.Cree un programa que elimine todos los números impares de una lista.

my_list = [12, 24,13, 27, 31, 36, 40,43, 49, 48]
new_list = []

for number in my_list:
    #print(number, " ", number % 2)
    if(number % 2 == 0):
        new_list.append(number);
print(new_list)

# 5.Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

max_number = 0
number_list = []

for counter in range(10):
    number_value = int(input(f"{counter + 1}-Type a number: "))
    if number_value > max_number:
        max_number = number_value
    number_list.append(number_value)

print(f"{number_list}. The highest number is: {max_number}")