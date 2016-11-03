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
        print((lambda num1, num2: num1 + num2)(num1, num2))
    elif (operator == "-"):
        print((lambda num1, num2: num1 - num2)(num1, num2))
    elif (operator == "*"):
        print((lambda num1, num2: num1 * num2)(num1, num2))
    elif (operator == "/" or operator == "//"):
        try:
            print((lambda num1, num2: num1 // num2)(num1, num2))
        except ZeroDivisionError:
            print("DIVISION BY ZERO. CALLING SPECIAL FORCES.")
    elif (operator == "%"):
        print((lambda num1, num2: num1 % num2)(num1, num2))
    elif (operator == "**"):
        print((lambda num1, num2: num1 ** num2)(num1, num2))
    else:
        print("Invalid operator")
