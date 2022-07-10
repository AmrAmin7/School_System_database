import database


SCHOOL_SYSTEM= f""" School system....


Please choose one of this option:

a) To add student.
d) To delete student's information.
u) To edit student's information.
s) To show student's information.
e) Exit

Your selection:
"""

def student():
    database.get_students()
    # print(database.get_students())
    while (user_input :=input(SCHOOL_SYSTEM).lower()) != "e":
        if user_input == "a":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            grade = int(input("Enter the grade:9 to 12:  "))
            database.add_student(first_name,last_name,grade)
            database.get_students()
            
        elif user_input == "d":
            id= input('Enter the id: ')
            database.delete_students(id)

        elif user_input == "u":
            id = input("Enter the id: ")
            grade = int(input("Enter the grade:9 to 12:  "))
            database.update_grade_students(grade,id)
                   
        elif user_input == "s":
            grade = int(input('Enter the grade:9 to 12: '))
            database.get_students_by_grade(grade)
                        
        else :
            print("Try again!")
  
student()
