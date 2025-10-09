import csv, os


def read_csv(path):
    students_list = []
    try:
        if not os.path.exists(path):
            print(f"-File '{path}' not found")
            
        else:
            with open(path,"r",encoding = "utf-8") as student_csv:
                reader = csv.DictReader(student_csv)
                for item in reader:
                    if item != []:
                        students_list.append(item)
                print("-Students imported successfully")    
    except Exception as ex:
        print(f"Error reading CSV: {ex}")
    
    return students_list


def import_csv(student_list):
    try:
        print(">> Import Students <<")
        import_path = input("File's path to import: ")
        import_csv = read_csv(import_path)
        return student_list + import_csv
    except Exception as ex:
        print(f"Error: {ex}")


def save_csv(paht, data):
    try:
        with open(paht, "w", encoding = "utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return True
    except Exception as ex:
        print(f"Error saving CSV: {ex}")
        return False