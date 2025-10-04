'''
1.Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
'''

hotel_dictionary = {
    "Name": "Luxury",
    "Stars": 7,
    "Rooms": [
        {
            "Number": 1,
            "Floor": 1,
            "Price": 200
        },
        {
            "Number": 2,
            "Floor": 1,
            "Price": 200
        },
        {
            "Number": 3,
            "Floor": 1,
            "Price": 200
        },
        {
            "Number": 4,
            "Floor": 1,
            "Price": 200
        },
        {
            "Number": 5,
            "Floor": 1,
            "Price": 200
        },
        {
            "Number": 6,
            "Floor": 2,
            "Price": 250
        },
        {
            "Number": 7,
            "Floor": 2,
            "Price": 250
        },
        {
            "Number": 8,
            "Floor": 2,
            "Price": 250
        },
        {
            "Number": 9,
            "Floor": 2,
            "Price": 250
        },
        {
            "Number": 10,
            "Floor": 2,
            "Price": 250
        },
        {
            "Number": 11,
            "Floor": 3,
            "Price": 300
        },
        {
            "Number": 12,
            "Floor": 3,
            "Price": 300
        },
        {
            "Number": 13,
            "Floor": 3,
            "Price": 300
        },
        {
            "Number": 14,
            "Floor": 3,
            "Price": 400
        },
        {
            "Number": 15,
            "Floor": 3,
            "Price": 400
        },
    ]
}

print(hotel_dictionary)

# 2.Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
new_dictionaty = {}

for counter in range(len(list_a)):
    new_dictionaty[list_a[counter]] = list_b[counter] 

print(new_dictionaty)

# 3.Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for item in list_of_keys:
    employee.pop(item)

print(employee)