
from datetime import datetime
student_list = []
now = datetime.now()
creation = now.strftime("%d/%m/%Y %H:%M:%S")

def calculate_average(_student_info):

    grades_sum = 0
    coefficient_sum = 0

    for grades in _student_info["Grades"]:
        grades_sum += grades["Grade"] * grades["Coefficient"]
        coefficient_sum += grades["Coefficient"]

    if coefficient_sum == 0:
        average = 0

    else:
        average = grades_sum / coefficient_sum
    return average


def crud_student(_splitted_data):

    student_info = {"Student no": _splitted_data[1], "Student name": _splitted_data[2], "Grades": []}
    student_list.append(student_info)


def crud_grades(_splitted_data):

    for student_info in student_list:
        if student_info["Student no"] == _splitted_data[1]:
            grades = ({"Lesson": _splitted_data[3], "Coefficient": len(_splitted_data[4]),
                       "Grade": int(_splitted_data[5]), "Created at": creation})
            student_info["Grades"].append(grades)



def print_data(student_no):

    for student_info in student_list:
        if student_info["Student no"] == student_no:
            print(f"Student No: {student_info['Student no']}")
            print(f"Student Name: {student_info['Student name']}")
            print(f"Average: {calculate_average(student_info)}")
            print("Grades:")
            for grade in student_info["Grades"]:
                print(f"Lesson: {grade['Lesson']}, Coefficient: {grade['Coefficient']}, "
                      f"Grade: {grade['Grade']}, Created at: {grade['Created at']}")
            return
