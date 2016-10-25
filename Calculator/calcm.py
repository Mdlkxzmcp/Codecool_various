adding_list = ["+", "plus", "add"]
subtracting_list = ["-", "minus", "subtract"]
multiplying_list = ["*", "multiply"]
dividing_list = ["/", "divide"]


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
        all_operations = ["+", "plus", "add", "-", "minus", "subtract", "*",
                          "multiply", "/", "divide"]
        decision = input("Enter desired operation: ")
        if(decision == "quit"):
            quit()
        elif(decision in all_operations):
            break
        else:
            print('This is not a valid operation here, choose one: ', end="")
            print(all_operations, end="")
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
class Math_Functions:

    def adding(num1, num2):
        global result
        result = num1 + num2
        print("Result: " + format(result))

    def subtracting(num1, num2):
        global result
        result = num1 - num2
        print("Result: " + format(result))

    def multiplying(num1, num2):
        global result
        result = num1 * num2
        print("Result: " + format(result))

    def dividing(num1, num2):
        global result
        result = num1 / num2
        print("Result: " + format(result))


def main():
    """the main function first calls question_handler and then uses its output
        to call the Math_Functions functions"""
    question_handler()
    if(decision in adding_list):
        Math_Functions.adding(num1, num2)
    elif(decision in subtracting_list):
        Math_Functions.subtracting(num1, num2)
    elif(decision in multiplying_list):
        Math_Functions.multiplying(num1, num2)
    elif(decision in dividing_list):
        Math_Functions.dividing(num1, num2)
    else:
        print("Unexpected situation, calling mentors...")

if __name__ == '__main__':
    main()
