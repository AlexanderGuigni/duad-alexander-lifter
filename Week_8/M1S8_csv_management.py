
'''
1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB
'''
import csv

def read_videogame_info():
    videogame = {
        "Name" : input("Name: "),
        "Geneder" : input("Geneder: "),
        "Developer" : input("Developer: "),
        "ESBR clasification" : input("ESBR clasification: ")
    }
    return videogame
    
    
def generate_csv_file(videogames_list, paht):
    try:
        with open(paht, "w", encoding = "utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, videogames_list[0].keys())
            writer.writeheader()
            writer.writerows(videogames_list)
    except Exception as ex:
        print(f"Error: {ex}")


def main_one():
    want_continue = True
    videogames_list = []
    while want_continue:
        videogames_list.append(read_videogame_info())
        try:
            res =input("Do you want to add another videogame (Yes = Y | No = N )")
            if res.upper() == "Y" or res.upper() == "YES":
                want_continue = True
            elif res.upper() == "N" or res.upper() == "NO":
                want_continue = False
            else:
                raise ValueError(f"{res} is not a valid option")
        except ValueError as ex:
            print(f"Error: {ex}")
            want_continue = False
    generate_csv_file(videogames_list, "Videogames.csv")


main_one()

#2. Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
import csv


def read_videogame_info():
    videogame = {
        "Name" : input("Name: "),
        "Geneder" : input("Geneder: "),
        "Developer" : input("Developer: "),
        "ESBR clasification" : input("ESBR clasification: ")
    }
    return videogame


def generate_csv_file_delimited_by_space(videogames_list, paht):
    try:
        with open(paht, "w", encoding = "utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, videogames_list[0].keys(), delimiter = "\t")
            writer.writeheader()
            writer.writerows(videogames_list)
    except Exception as ex:
        print(f"Error: {ex}")


def main_two():
    want_continue = True
    videogames_list = []
    while want_continue:
        videogames_list.append(read_videogame_info())
        try:
            res =input("Do you want to add another videogame (Yes = Y | No = N )")
            if res.upper() == "Y" or res.upper() == "YES":
                want_continue = True
            elif res.upper() == "N" or res.upper() == "NO":
                want_continue = False
            else:
                raise ValueError(f"{res} is not a valid option")
        except ValueError as ex:
            print(f"Error: {ex}")
            want_continue = False
    generate_csv_file_delimited_by_space(videogames_list, "Videogames2.csv")


main_two()