def add(num1, num2):
    print(num1 + num2)


def subtract(num1, num2):
    print(num1 - num2)


def multiply(num1, num2):
    print(num1 * num2)


def divide(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("You can't divide by zero you silly goose :>")


def reminder(num1, num2):
    print(num1 % num2)


def power(num1, num2):
    print(num1 ** num2)


def numbers(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            quit()

while True:

    first_number = numbers("Enter a number(or a letter to exit): ")
    operator = input("Enter an operator: ")
    second_number = numbers("Enter another number: ")

    if operator == "+":
        add(first_number, second_number)
    elif operator == "-":
        subtract(first_number, second_number)
    elif operator == "*":
        multiply(first_number, second_number)
    elif operator == "/" or operator == "//":
        divide(first_number, second_number)
    elif operator == "%":
        reminder(first_number, second_number)
    elif operator == "**":
        power(first_number, second_number)
    else:
        print("Invalid operator")
