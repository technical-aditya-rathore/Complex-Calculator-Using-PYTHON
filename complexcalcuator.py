import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    else:
        return math.sqrt(x)


def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    else:
        return math.log(x, base)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number is undefined."
    else:
        return math.factorial(x)


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")

    while True:
        choice = input("Enter choice (1-11): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {power(num1, num2)}")

        elif choice in ['6', '7', '8', '9', '10', '11']:
            num = float(input("Enter number: "))

            if choice == '6':
                print(f"The result is: {square_root(num)}")
            elif choice == '7':
                base = float(
                    input("Enter logarithm base (default is 10): ") or 10)
                print(f"The result is: {logarithm(num, base)}")
            elif choice == '8':
                print(f"The result is: {sine(num)}")
            elif choice == '9':
                print(f"The result is: {cosine(num)}")
            elif choice == '10':
                print(f"The result is: {tangent(num)}")
            elif choice == '11':
                print(f"The result is: {factorial(int(num))}")

        else:
            print("Invalid Input")

        next_calculation = input(
            "Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break


if __name__ == "__main__":
    calculator()
