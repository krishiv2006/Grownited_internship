class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def __str__(self):
        return (
            f"ID      : {self.student_id}\n"
            f"Name    : {self.name}\n"
            f"Age     : {self.age}\n"
            f"Course  : {self.course}\n"
            f"Email   : {self.email}"
        )