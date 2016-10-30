def add(num1, num2):
    print(num1 + num2)


def subtract(num1, num2):
    print(num1 - num2)


def multiply(num1, num2):
    print(num1 * num2)


def divide(num1, num2):
    print(num1 // num2)


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

    num1 = numbers("Enter a number(or a letter to exit): ")
    operator = input("Enter an operator: ")
    num2 = numbers("Enter another number: ")

    if (operator == "+"):
        add(num1, num2)
    elif (operator == "-"):
        subtract(num1, num2)
    elif (operator == "*"):
        multiply(num1, num2)
    elif (operator == "/" or operator == "//"):
        divide(num1, num2)
    elif (operator == "%"):
        reminder(num1, num2)
    elif (operator == "**"):
        power(num1, num2)
    else:
        print("Invalid operator")
