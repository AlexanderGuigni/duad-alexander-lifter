# 1. Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def open_file_get_phrase(path):
    try:
        with open(path) as phrase_file:
            return phrase_file.readlines()
    except Exception as ex:
        print(f"Error Reading: {ex}")


def create_new_file_with_one_line(phrase, path):
    try:
        with open(path, "w") as one_line_file:
            one_line_file.write(phrase)
    except Exception as ex:
        print(f"Error Writing: {ex}")


def main_one():
    try:
        phrase_list = open_file_get_phrase("PhraseInLines.txt")
        phrase = ""
        for line in phrase_list:
            phrase = phrase + line.replace("\n", " ")
        create_new_file_with_one_line(phrase, "PhraseInOneLine.txt")
    except Exception as ex:
        print(f"Error: {ex}")



main_one()

# 2.Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.

def open_file_get_all_text(path):
    try:
        with open(path) as phrase_file:
            return phrase_file.read()
    except Exception as ex:
        print(f"Error Reading: {ex}")

def get_total_of_words(strng_to_count):
    try:
        word_list = strng_to_count.replace("\n", " ").split(" ")
        #print(word_list)
        return len(word_list)
    except ExceptionGroup as ex:
        print(f"Error: {ex}")

def main_two():
    try:
        strng = open_file_get_all_text("Text.txt")
        print(get_total_of_words(strng))
    except Exception as ex:
        print(f"Error: {ex}")

main_two()

# 1. Cree un programa que:
'''
- Lea un archivo línea por línea
- Convierta cada línea a **mayúsculas**
- Escriba el contenido en un **nuevo archivo**
'''

def open_file_get_lines(path):
    try:
        with open(path) as new_file:
            return new_file.readlines()
    except Exception as ex:
        print(f"Error Reading: {ex}")


def create_new_file(upper_text, path):
    try:
        with open(path, "w") as new_file:
            new_file.write(upper_text)
    except Exception as ex:
        print(f"Error Writing: {ex}")


def main_three():
    try:
        lines_list = open_file_get_all_text("Text.txt")
        upper_string = ""
        for line in lines_list:
            upper_string = upper_string + line.upper()
        create_new_file(upper_string, "UpperText.txt")
    except Exception as ex:
        print(f"Error: {ex}")

main_three()

# 4. Cree un programa que:
'''
- Pida al usuario una línea de texto
- Agregue esa línea **al final** de un archivo existente
- Si el archivo no existe, lo crea automáticamente
'''
def add_text_to_a_file(text, path):
    try:
        with open(path, "a", encoding = "utf-8") as new_file:
            new_file.write(text)
            new_file.write("\n")
    except Exception as ex:
        print(f"Error Writing: {ex}")

def main_four():
    try:
        text_line = input("Type a text line: ")
        add_text_to_a_file(text_line, "TextFile.txt")
    except Exception as ex:
        print(f"Error: {ex}")

main_four()