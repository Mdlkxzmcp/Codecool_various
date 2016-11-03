ADDING_LIST = ("+", "plus", "add")
SUBTRACTING_LIST = ("-", "minus", "subtract")
MULTIPLYING_LIST = ("*", "multiply", "times")
DIVIDING_LIST = ("/", "divide")


def question_handler():
    """this function handles the user input"""
    global num1, num2, decision
    # while blocks that check if the input is of valid type
    while True:
        try:
            num1 = int(input("Enter the first number you want to work with: "))
        # if the input cannot be made into a number this happenes
        except ValueError:
            print("Why are you playing around?")
            continue
        else:
            break
    while True:
        ALL_OPERATIONS = ("+", "plus", "add", "-", "minus", "subtract", "*",
                          "multiply", "times", "/", "divide")
        decision = input("Enter desired operation: ")
        if(decision == "quit"):
            quit()
        elif(decision in ALL_OPERATIONS):
            break
        else:
            print('This is not a valid operation here, choose one: ', end="")
            print(ALL_OPERATIONS, end="")
            print(" or type in \"quit\" to exit")
    while True:
        try:
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Hey stop that!")
            continue
        else:
            break


# making use of classes here just for fun
class MathFunctions:

    def adding(num1, num2):
        result = num1 + num2
        print("Result: " + format(result))

    def subtracting(num1, num2):
        result = num1 - num2
        print("Result: " + format(result))

    def multiplying(num1, num2):
        result = num1 * num2
        print("Result: " + format(result))

    def dividing(num1, num2):
        result = num1 / num2
        print("Result: " + format(result))


def main():
    """the main function first calls question_handler and then uses its output
        to call the MathFunctions functions"""
    question_handler()
    calc = MathFunctions(num1, num2)
    if(decision in ADDING_LIST):
        MathFunctions.adding(num1, num2)
    elif(decision in SUBTRACTING_LIST):
        MathFunctions.subtracting(num1, num2)
    elif(decision in MULTIPLYING_LIST):
        MathFunctions.multiplying(num1, num2)
    elif(decision in DIVIDING_LIST):
        MathFunctions.dividing(num1, num2)
    else:
        print("Unexpected situation, calling mentors...")

if __name__ == '__main__':
    main()
