import csv, os
from Student import Student


def read_csv(path):
    students_list = []
    try:
        if not os.path.exists(path):
            print(f"-File '{path}' not found")
            
        else:
            with open(path,"r",encoding = "utf-8") as student_csv:
                reader = csv.DictReader(student_csv)
                for item in reader:
                    student = Student(item.get("full_name"), item.get("section"), item.get("spanish_grade"), item.get("english_grade"), item.get("social_grade"), item.get("science_grade"))
                    students_list.append(student)
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


def convert_from_student_to_dictionary(students_list):
    students_dic_list = []
    try:
        for student in students_list:
            students_dic = {"full_name" : student.full_name,
            "section" : student.section,
            "spanish_grade" : student.spanish_grade,
            "english_grade" : student.english_grade,
            "social_grade" : student.social_grade,
            "science_grade" : student.science_grade}
            students_dic_list.append(students_dic)
        print("-Converted")
    except Exception as ex:
        print(f"Error converting list to dictionary: {ex}")
    return(students_dic_list)



def save_csv(paht, data):
    try:
        data = convert_from_student_to_dictionary(data)
        with open(paht, "w", encoding = "utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return True
    except Exception as ex:
        print(f"Error saving CSV: {ex}")
        return False