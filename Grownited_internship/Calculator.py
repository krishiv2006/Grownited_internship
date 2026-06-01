# Calculator with 15 Functionalities

print("===== PYTHON CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7. Floor Division")
print("8. Square")
print("9. Cube")
print("10. Square Root")
print("11. Greater Number")
print("12. Smaller Number")
print("13. Even or Odd")
print("14. Percentage")
print("15. Exit")

choice = int(input("Enter your choice (1-15): "))

if choice == 15:
    print("Calculator Closed")

elif choice in [8, 9, 10, 13]:
    num = float(input("Enter a number: "))

    if choice == 8:
        print("Square =", num * num)

    elif choice == 9:
        print("Cube =", num * num * num)

    elif choice == 10:
        print("Square Root =", num ** 0.5)

    elif choice == 13:
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero not allowed")

    elif choice == 5:
        print("Result =", num1 % num2)

    elif choice == 6:
        print("Result =", num1 ** num2)

    elif choice == 7:
        print("Result =", num1 // num2)

    elif choice == 11:
        if num1 > num2:
            print("Greater Number =", num1)
        else:
            print("Greater Number =", num2)

    elif choice == 12:
        if num1 < num2:
            print("Smaller Number =", num1)
        else:
            print("Smaller Number =", num2)

    elif choice == 14:
        percentage = (num1 / num2) * 100
        print("Percentage =", percentage, "%")

    else:
        print("Invalid Choice")