from Student import Student


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_from_file()

    def add_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty")
            return

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0")
                return

        except ValueError:
            print("Invalid Age")
            return

        course = input("Enter Course: ")

        email = input("Enter Email: ")

        if "@" not in email:
            print("Invalid Email")
            return

        student = Student(student_id, name, age, course, email)

        self.students.append(student)

        print("Student Added Successfully")

    def search_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found")
                print(student)
                return

        print("Student Not Found")

    def delete_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully")
                return

        print("Student Not Found")

    def display_students(self):

        if len(self.students) == 0:
            print("No Students Available")
            return

        for student in self.students:
            print("---------------------------------")
            print(student)
            print("---------------------------------")

    def save_to_file(self):

        with open("students.txt", "w") as file:

            for student in self.students:

                file.write(
                    f"{student.student_id},"
                    f"{student.name},"
                    f"{student.age},"
                    f"{student.course},"
                    f"{student.email}\n"
                )

        print("Data Saved Successfully")

    def load_from_file(self):

        try:

            with open("students.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 5:

                        student = Student(
                            data[0],
                            data[1],
                            int(data[2]),
                            data[3],
                            data[4]
                        )

                        self.students.append(student)

        except FileNotFoundError:
            pass