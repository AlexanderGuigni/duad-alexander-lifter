import actions, data


def display_menu():
    print(">>  Main menu  <<")
    print("1. Enter student information")
    print("2. Delete student information")
    print("3. View students information")
    print("4. View top 3 of the highest grade averages")
    print("5. View reproved students")
    print("6. View total grades average")
    print("7. Export existing students information to CSV")
    print("8. Import students (.csv file)")
    print("9. Exit")


def get_menu_option():
    menu_options = [1,2,3,4,5,6,7,8,9]
    option_selected = input("Desired menu option: ")
    is_valid_option = False
    try:
        option_selected = int(option_selected)
        if option_selected in menu_options:
            is_valid_option = True
        else:
            raise ValueError
    except ValueError as ex:
        print(f"The option selected ({option_selected}) is not valid")

    return [option_selected, is_valid_option]


def run_menu_option(menu_option):
    show_menu_again = True
    try:
        students_list = []
        if(menu_option[1] != False):
            if menu_option[0] == 1:
                add_more = True
                while add_more:
                    students_list = data.read_csv("Data\students.csv")
                    student_info = actions.get_student_info()
                    students_list.append(student_info)
                    if data.save_csv("Data\students.csv",students_list):
                        print(f"-Student {student_info["full_name"]} added successfully")
                        add_more = actions.validate_if_reppeat_action("Do you want to add another student?")
            elif menu_option[0] == 2:
                delete_more = True
                while delete_more:
                    students_list = data.read_csv("Data\students.csv")
                    students_list = actions.delete_student(students_list)
                    if students_list != None and data.save_csv("Data\students.csv",students_list[0]):
                        print(f"-Student {students_list[1]["full_name"]} was deleted successfully")
                    delete_more = actions.validate_if_reppeat_action("Do you want to delete another student?")
            elif menu_option[0] == 3:
                students_list = data.read_csv("Data\students.csv")
                actions.display_students_infromation(students_list)
            elif menu_option[0] == 4:
                students_list = data.read_csv("Data\students.csv")
                actions.dispaly_highest_grade_averages(students_list)
            elif menu_option[0] == 5:
                students_list = data.read_csv("Data\students.csv")
                actions.display_reproved_students(students_list)
            elif menu_option[0] == 6:
                students_list = data.read_csv("Data\students.csv")
                actions.display_total_grades_average(students_list)
            elif menu_option[0] == 7:
                students_list = data.read_csv("Data\students.csv")
                if students_list != []:    
                    if data.save_csv("Data\Exported\students_exported.csv", students_list):
                        print("-Students exported successfully to Exported folder")
                else:
                    print("-No entries to export")
            elif menu_option[0] == 8:
                students_list = data.read_csv("Data\students.csv")
                students_list = data.import_csv(students_list)
                if data.save_csv("Data\students.csv", students_list):
                    print("-Students imported successfully")
            elif menu_option[0] == 9:
                show_menu_again = False

            if menu_option[0] != 9:
                print("")
                input("Type any key to continue")
                print("")
    except Exception as ex:
        print(f"Error: {ex}")  
    return show_menu_again          