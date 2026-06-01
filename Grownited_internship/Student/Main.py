from StudentManager import StudentManager

manager = StudentManager()

while True:

    print("\n=================================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Save Data To File")
    print("6. Exit")

    try:

        choice = int(input("Enter Choice: "))

        if choice == 1:
            manager.add_student()

        elif choice == 2:
            manager.search_student()

        elif choice == 3:
            manager.delete_student()

        elif choice == 4:
            manager.display_students()

        elif choice == 5:
            manager.save_to_file()

        elif choice == 6:
            manager.save_to_file()
            print("Program Closed")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number")