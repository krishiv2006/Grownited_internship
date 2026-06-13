import numpy as np

students = np.array([
    "Amit",
    "Neha",
    "Rahul",
    "Priya",
    "Karan",
    "Sneha",
    "Jay",
    "Riya"
])

marks = np.array([
    45,
    78,
    92,
    67,
    55,
    88,
    34,
    95
])

print("Task 1: Display Student Data")
for i in range(len(students)):
    print(students[i], ":", marks[i])

print("\nTask 2: Calculate Total Marks")
total_marks = np.sum(marks)
print("Total Marks =", total_marks)

print("\nTask 3: Calculate Average Marks")
average_marks = np.mean(marks)
print("Average Marks =", average_marks)

print("\nTask 4: Find Highest Scorer")
highest_marks = np.max(marks)
topper = students[np.argmax(marks)]
print("Highest Marks =", highest_marks)
print("Topper =", topper)

print("\nTask 5: Find Lowest Scorer")
lowest_marks = np.min(marks)
lowest_student = students[np.argmin(marks)]
print("Lowest Marks =", lowest_marks)
print("Student =", lowest_student)

print("\nTask 6: Pass and Fail Analysis")
passed = students[marks >= 40]
failed = students[marks < 40]

print("Passed Students:")
for student in passed:
    print(student)

print("\nFailed Students:")
for student in failed:
    print(student)

print("\nTask 7: Students Above Average")
print("Students Above Average:")
for student in students[marks > average_marks]:
    print(student)

print("\nTask 8: Grade Assignment")
for i in range(len(marks)):
    if marks[i] >= 90:
        grade = "A"
    elif marks[i] >= 75:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    elif marks[i] >= 40:
        grade = "D"
    else:
        grade = "F"

    print(students[i], ":", grade)

print("\nTask 9: Top 3 Students")
sorted_indices = np.argsort(marks)[::-1]

for i in sorted_indices[:3]:
    print(students[i], marks[i])

print("\nTask 10: Class Statistics")
print("Highest Marks :", np.max(marks))
print("Lowest Marks :", np.min(marks))
print("Average Marks :", np.mean(marks))
print("Median Marks :", np.median(marks))
print("Standard Deviation :", round(np.std(marks), 2))

print("\n==================================")
print("STUDENT PERFORMANCE REPORT")
print("Total Students :", len(students))

print("\nHighest Marks :", highest_marks)
print("Topper :", topper)

print("\nLowest Marks :", lowest_marks)
print("Lowest Performer :", lowest_student)

print("\nAverage Marks :", round(average_marks, 2))

pass_percentage = (len(passed) / len(students)) * 100
print("\nPass Percentage :", pass_percentage, "%")

print("\nScholarship Students :")
for student in students[marks >= 85]:
    print(student)

print("\nTop 3 Students :")
for i in sorted_indices[:3]:
    print(students[i], "-", marks[i])

print("\n==================================")
print("END OF REPORT")