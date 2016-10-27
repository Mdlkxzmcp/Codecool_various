import random
import datetime

global current_capital
used_letters = []
life = 5


def file_operator():
    global current_capital
    global current_capital_upper
    global current_country
    with open("countries_and_capitals.txt") as list:
        countries_and_capitals = list.read().splitlines()
        choosen_pair = random.choice(countries_and_capitals)
        current_capital = choosen_pair.split("| ")[1]
        current_capital_upper = current_capital.upper()
        current_country = choosen_pair.split("| ")[0]


def show_status(current_capital_upper):
    global used_letters
    current_life()
    if checker(used_letters, current_capital_upper) is True:
        win_screen()
    else:
        for letter in current_capital_upper:
            if letter in used_letters:
                print(letter, end="")
            else:
                print("_ ", end="")
        if used_letters:
            print(used_letters)


def win_screen():
    print("Congratulations! You won!!!!")
    try_again()


def try_again():
    try_again = input("Do you want to try again? yes/no: ")
    if try_again == "yes" or try_again == "y":
        main()
    elif try_again == "no" or try_again == "n":
        quit()
    else:
        print("yes or no")
        try_again()


def loose_screen():
    print("Welp")
    try_again()


def current_life():
    global life
    print("Remaining life: ", life)


def letter_input():
    global life
    choosen_letter = input("Type in a letter: ").upper()
    if choosen_letter in used_letters:
        print("You already used this letter")
        letter_input()
    else:
        used_letters.append(choosen_letter)
    if choosen_letter not in current_capital_upper:
        life -= 1


def word_input():
    global life
    choosen_word = input("Type in a word: ")
    if choosen_word == current_capital_upper:
        win_screen()
    else:
        life -= 2


def input_situation():
    choice = input("Do you want to type in a (l)etter or a (w)ord?: ")
    if choice == "letter" or choice == "l":
        letter_input()
    elif choice == "word" or choice == "w":
        word_input()
    else:
        print("That's not an option.")
        input_situation()


def checker(used_letters, current_capital_upper):
    return set(current_capital_upper).issubset(used_letters)


def main():
    global life
    global used_letters
    file_operator()
    while True:
        if life > 0:
            show_status(current_capital_upper)
            input_situation()
        else:
            loose_screen()
"""
if input == current_capital_upper:
    print("you won!")
else:
"""
if __name__ == '__main__':
    main()
