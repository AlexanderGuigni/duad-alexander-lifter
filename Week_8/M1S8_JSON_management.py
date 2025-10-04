#1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
'''
2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
'''
import json

def read_joson_file(path):
    try: 
        with open(path, "r",encoding = "utf=8") as josn_info:
            return josn_info.read()
    except Exception as ex:
        print(f"Error: {ex}")

def ask_new_pokemon_info():
    try: 
        print("<<< New Pokeon info >>>")
        return {'name': {'english': input("Name: ")}, 'type': [input("Type: ")], 'base': {'HP': int(input("HP: ")), 'Attack': int(input("Attack: ")), 'Defense': int(input("Defense: ")), 'Sp. Attack': int(input("Sp. Attack: ")), 'Sp. Defense': int(input("Sp. Defense: ")), 'Speed': int(input("Speed: "))}}
    except ValueError as ex:
        print(f"Error: {ex}")

def write_json(dic_list,path):
    try:
        with open(path, "w", encoding = "utf-8") as json_file:
            json_file.write(dic_list)
    except Exception as ex:
        print(f"Error: {ex}")


def main():
    try:
        poke_dic_list = json.loads(read_joson_file("Pokemons.json"))
        poke_dic_list.append(ask_new_pokemon_info())
        print(poke_dic_list) 
        write_json(json.dumps(poke_dic_list), "Pokemons.json")
    except Exception as ex:
        print(f"Error: {ex}")


main()