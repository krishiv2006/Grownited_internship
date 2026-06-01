# Student Grade System

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


name = input("Enter Student Name: ")
marks = float(input("Enter Student Marks: "))

grade = calculate_grade(marks)

print("\n----- Result -----")
print("Name :", name)
print("Marks :", marks)
print("Grade :", grade)