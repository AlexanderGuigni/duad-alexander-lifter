import re


def get_name():
    name = input("Full Name: ")
    try:
        if  name.replace(" ", "").isalpha():
            return name
        else:
            raise ValueError
    except ValueError:
        print("Error getting the student's name: The Student name must not be empty and cant content numbers")
        return get_name()


def get_section():
    section = input("Section: ")
    pattern = r"^[0-9]{2}[A-Z]$"
    try:
        if  re.match(pattern,section):
            return section
        else:
            raise ValueError
    except ValueError:
        print("Error getting the student's name: Section format is not valid (Examples: 01A, 11B, 05C)")
        return get_section()


def get_grade(grade_name):
    grade = input(f"{grade_name}: ")
    try:
        grade = float(grade)
        if grade > 0 and grade <=100:
            return grade
        else:
            raise ValueError
    except ValueError:
        print(f"Error getting the grade: Value entered must be between 1 and 100")
        return get_grade(grade_name)

def get_student_info():
    print(">> New student <<")
    students = {"full_name" : get_name(),
        "section" : get_section(),
        "spanish_grade" : get_grade("Spanish grade"),
        "english_grade" : get_grade("English grade"),
        "social_grade" : get_grade("Social grade"),
        "science_grade" : get_grade("Science grade")}
    return students


def delete_student(student_list):
    print(">> Delete student <<")
    student_to_delete = {"full_name" : get_name(), "section" : get_section()}
    try:
        for index,student in enumerate(student_list):
            if student["full_name"] == student_to_delete["full_name"] and student["section"] == student_to_delete["section"]:
                print("-Student found")
                student_list.pop(index)
                return [student_list, student_to_delete]
            elif index == len(student_list)-1:
                print("-Student not found")
                return None
    except Exception as ex:
        print(f"Error deleting student: {ex}")
        return None



def display_students_infromation(students_list):
    counter = 1
    if students_list != []:
        try:
            print(">> Students list <<")
            print("")
            for student in students_list:
                print(f"{counter}. {student.get("full_name")}")
                counter = counter + 1
                print(f"> Section: {student.get("section")}")
                print("> Grades")
                print(f"   Spanish: {student.get("spanish_grade")}")
                print(f"   English: {student.get("english_grade")}")
                print(f"   Social: {student.get("social_grade")}")
                print(f"   Science: {student.get("science_grade")}")
                print("")
        except Exception as ex:
            print(f"Error displaying the student list: {ex} ")
    else:
        print("-Any student registered")

def calculate_student_average(student_info):
    average = 0

    try:
        average = (float(student_info.get("spanish_grade")) + float(student_info.get("english_grade")) + float(student_info.get("social_grade")) + float(student_info.get("science_grade"))) / 4
    except Exception as ex:
        print(f"Error calculating grade average of {student_info.get("full_name")}: {ex}" )

    return round(average,2)


def dispaly_highest_grade_averages(students_list):
    average_1 = [{},0]
    average_2 = [{},0]
    average_3 = [{},0]
    if students_list != []:
        try:
            for student in students_list:
                average = calculate_student_average(student)
                #student["average"] = average
                if average > average_1[1]:
                    average_3 = average_2
                    average_2 = average_1
                    average_1 = [student,average]
                elif average > average_2[1]:
                    average_3 = average_2
                    average_2 = [student,average]
                elif average > average_3[1]:
                    average_3 = [student,average]
        except Exception as ex:
            print(f"Error getting highest grade averages: {ex}")
        
        print("")
        print(">> Student with the highest grade averages <<")
        print("")

        counter = 1
        
        for student in [average_1, average_2, average_3]:
            if student != [{},0]:
                print(f"{counter}. Student {student[0].get("full_name")} with average {student[1]}")
                counter = counter + 1
                print(f"> Section: {student[0].get("section")}")
                print("> Grades")
                print(f"   Spanish: {student[0].get("spanish_grade")}")
                print(f"   English: {student[0].get("english_grade")}")
                print(f"   Social: {student[0].get("social_grade")}")
                print(f"   Science: {student[0].get("science_grade")}")
                print("")
    else:
        print("-Any student registered")


def display_reproved_students(students_list):
    counter = 1
    if students_list != []:
        try:
            print("")
            print(">> Students reproved <<")
            print("")
            for student in students_list:
                if (float(student.get("spanish_grade")) < 60 or float(student.get("english_grade")) < 60 or float(student.get("social_grade")) < 60 or float(student.get("science_grade")) < 60):
                    print(f"{counter}. Student {student.get("full_name")} from section: {student.get("section")}")
                    counter = counter + 1
        except Exception as ex:
            print(f"Error displaying reproved the student list: {ex} ")
    else:
        print("-Any student registered")


def display_total_grades_average(students_list):
    total_grades_average = 0
    if students_list != []:    
        try:
            for student in students_list:
                total_grades_average = total_grades_average + calculate_student_average(student)
            total_grades_average = total_grades_average / len(students_list)
        except Exception as ex:
            print(f"Error displaying total grades average: {ex}")

        print(">> Total grades average <<")
        print(f"Total average: {round(total_grades_average,2)}")
    else:
        print("-Any student registered")


def validate_if_reppeat_action(message):
    response = input(f"{message} (Yes = Y / No / N): ")
    try:
        if response.upper() == "Y" or response.upper == "YES":
            return True
        elif response.upper() == "N" or response.upper == "NO":
            return False
        else:
            raise ValueError
    except ValueError:
        print(f"Option selected ({response}) is not valid option")
        return validate_if_reppeat_action(message)