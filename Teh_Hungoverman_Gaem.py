import random

global current_capital
used_letters = []
life = 5

with open("european_capitals") as list:
    euro_capitals = list.read().splitlines()


def random_capital(euro_capitals):
    current_capital = random.choice(euro_capitals)
    return current_capital


def show_status(choosen_capital):
    global used_letters
    current_life()
    if checker(used_letters, choosen_capital) is True:
        win_screen()
    else:
        for letter in choosen_capital:
            if letter in used_letters:
                print(letter, end="")
            else:
                print("_ ", end="")
        if used_letters:
            print(used_letters)


def win_screen():
    print("Congratulations! You won!!!!")
    quit()


def loose_screen():
    print("Welp")
    try_again = input("Do you want to try again? yes/no: ")
    if try_again == "yes" or try_again == "y":
        main()
    elif try_again == "no" or try_again == "n":
        quit()
    else:
        print("yes or no")
        loose_screen()


def current_life():
    global life
    print("Remaining life: ", life)


def input_situation(choosen_capital):
    global life
    global used_letters
    choice = input("Do you want to type in a (l)etter or a (w)ord?: ")
    if choice == "letter" or choice == "l":
        choosen_letter = input("Type in a letter: ").upper()
        if choosen_letter in used_letters:
            print("You already used this letter")
            input_situation(used_letters, choosen_capital)
        else:
            used_letters.append(choosen_letter)
        if choosen_letter not in choosen_capital:
            life -= 1
        """if "".join(used_letters) in choosen_capital:
            win_screen()"""
    elif choice == "word" or choice == "w":
        choosen_word = input("Type in a word: ").upper()
        if choosen_word == choosen_capital:
            win_screen()
        else:
            life -= 2
    else:
        print("That's not an option.")
        input_situation(used_letters, choosen_capital)


def checker(used_letters, choosen_capital):
    return set(choosen_capital).issubset(used_letters)


def main():
    global life
    global used_letters
    choosen_capital = random_capital(euro_capitals)
    while True:
        if life > 0:
            show_status(choosen_capital)
            input_situation(choosen_capital)
        else:
            loose_screen()
"""
if input == choosen_capital:
    print("you won!")
else:
"""
if __name__ == '__main__':
    main()
