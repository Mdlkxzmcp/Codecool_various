import random


def intro():
    print("""I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:

    When I say:    That means:

    Cold       No digit is correct.

    Warm       One digit is correct but in the wrong position.

    Hot        One digit is correct and in the right position.

    I have thought up a number. You have 10 guesses to get it.""")


def number_generator():
    available = []
    for number in range(0, 10):
        available.append(number)
    first_number = random.choice(available)
    available.remove(first_number)
    second_number = random.choice(available)
    available.remove(second_number)
    third_number = random.choice(available)
    available.remove(third_number)
    the_number = (first_number, second_number, third_number)
    return the_number


def number_pick(the_number):
    try_number = 1
    while True:
        if try_number > 10:
            print("\nYou tried but you failed.\n\n")
            success = "no"
            return False, success
        guessed_number = []
        guess = input("\nGuess #{}: ".format(try_number))
        if len(guess) == 3:
            try:
                for number in guess:
                    guessed_number.append(int(number))
            except ValueError:
                print("only numbers please~")
            tuple_number = tuple(guessed_number)
            if the_number == tuple_number:
                success = "yes"
                return False, success
            else:
                for index, value in enumerate(tuple_number):
                    if tuple_number[index - 1] == the_number[index - 1]:
                        print("Hot ", end="")
                    elif tuple_number[index - 1] in the_number:
                        print("Warm ", end="")
                    elif tuple_number[index - 1] not in the_number:
                        print("Cold ", end="")
                try_number += 1
        else:
            print("\nOnly 3 numbers please!\n")
    return success


def main():
    intro()
    success = number_pick(number_generator())
    if success[1] == "yes":
        print("You got it!\n")
    elif success[1] == "no":
        print("You have failed, how sad :,c")
    play_again = input("Do you want to play again? (yes or no) ")
    if play_again in ("yes", "y"):
        main()
    else:
        pass

if __name__ == '__main__':
    main()
