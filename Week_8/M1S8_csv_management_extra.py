'''
1. Cree un programa que abra un archivo `.csv` con la información de videojuegos (el que fue generado en el ejercicio 1) y:
- Lea cada línea usando `csv.reader()`
- Muestre el contenido en pantalla de forma legible, línea por línea
- Ejemplo:
'''

import csv

def main_one(path):
    counter = 1
    try:
        with open(path, "r",encoding = "utf-8") as csv_file:
            csv_rows = csv.reader(csv_file)
            next(csv_rows,None)
            for game in csv_rows:
                if game == []:
                    continue 
                print(f"Videogame #{counter}")
                counter = counter + 1
                print(f"  Name: {game[0]}")
                print(f"  Geneder: {game[1]}")
                print(f"  Developer: {game[2]}")
                print(f"  ESBR clasification: {game[3]}")
    except Exception as ex:
        print(f"Error: {ex}")


main_one("Videogames.csv")

'''
2. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo CSV de videojuegos
- Pida al usuario una clasificación ESRB (por ejemplo: "T")
- Muestre todos los videojuegos que tengan esa clasificación
'''
import csv

def main_two(path):
    counter = 1
    clasification = input("Type the clasification of the games you want to see: ")
    try:
        with open(path, "r",encoding = "utf-8") as csv_file:
            csv_rows = csv.reader(csv_file)
            next(csv_rows,None)
            for game in csv_rows:
                if game == [] or game[3] != clasification:
                    continue 
                print(f"Videogame #{counter}")
                counter = counter + 1
                print(f"  Name: {game[0]}")
                print(f"  Geneder: {game[1]}")
                print(f"  Developer: {game[2]}")
                print(f"  ESBR clasification: {game[3]}")
    except Exception as ex:
        print(f"Error: {ex}")


main_two("Videogames.csv")

'''
3. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Cuente cuántos videojuegos hay de **cada género**
- Muestre el resultado de forma ordenada
'''
import csv

def main_three(path):
    games_count = {}
    try:
        with open(path, "r",encoding = "utf-8") as csv_file:
            csv_rows = csv.reader(csv_file)
            next(csv_rows,None)
            for game in csv_rows:
                if game == []:
                    continue 
                if games_count.get(game[3]) == None:
                    games_count[game[3]] = 1
                else:
                    games_count[game[3]] = int(games_count.get(game[3])) + 1
            for clasification, total in games_count.items():
                print(f"{clasification}: {total}")
    except Exception as ex:
        print(f"Error: {ex}")


main_three("Videogames.csv")

'''
4. Cree un programa que abra un archivo `.csv` con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Pida al usuario ingresar el nombre de un **desarrollador** (ej. `"Ubisoft"`)
- Muestre todos los videojuegos desarrollados por esa empresa en formato legible
'''
import csv

def main_four(path):
    counter = 1
    developer = input("Type the developer of the games you want to see: ")

    print(f"Videogames develped by {developer}")

    try:
        with open(path, "r",encoding = "utf-8") as csv_file:
            csv_rows = csv.reader(csv_file)
            next(csv_rows,None)
            for game in csv_rows:
                if game == [] or game[2] != developer:
                    continue 
                print(f" > {game[0]} ({game[1]}, {game[2]}, {game[3]})")
                counter = counter + 1
    except Exception as ex:
        print(f"Error: {ex}")


main_four("Videogames.csv")