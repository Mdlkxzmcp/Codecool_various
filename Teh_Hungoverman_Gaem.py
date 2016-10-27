import random
import time
import datetime

global current_capital


def file_operator():
    global countries_and_capitals
    with open("countries_and_capitals.txt") as list:
        countries_and_capitals = list.read().splitlines()


def current_setter():
    global countries_and_capitals
    global current_capital
    global current_capital_upper
    global current_country
    choosen_pair = random.choice(countries_and_capitals)
    current_capital = choosen_pair.split("| ")[1]
    current_capital_upper = current_capital.upper()
    current_country = choosen_pair.split(" |")[0]


def high_score_screen():
    global high_scores
    with open("high_scores.txt") as list:
        high_scores = list.read().splitlines()
        print("\n".join(high_scores))


def clear():
    global life
    global used_letters
    used_letters = []
    life = 5


def show_status(current_capital_upper):
    global current_country
    global used_letters
    global life
    current_life()
    if life == 1:
        print("It's the capital of", current_country, ";3")
    for letter in current_capital_upper:
        if letter in used_letters:
            print(letter, end="")
        else:
            print("_ ", end="")
    if used_letters:
        print("  You already tired: ", used_letters)


def win_screen():
    global letters_count
    global current_capital
    global start_time
    global usable_elapsed_time
    elapsed_time = time.time() - start_time
    usable_elapsed_time = str(elapsed_time)[:4]
    print("Congratulations! You won using", letters_count,
          "letters! in", usable_elapsed_time, "sec, nice!")
    high_score_handler()
    try_again()


def high_score_handler():
    global usable_elapsed_time
    player_name = input("Type in your name to add it to the high scores!: ")
    new_high_score = [player_name, " | ", usable_elapsed_time, " | ",
                      str(letters_count), " | ", current_capital, "\n"]
    print("".join(new_high_score))
    with open("high_scores.txt", "a+") as high_scores:
        high_scores.writelines(new_high_score)


def try_again():
    global life
    high_score_screen()
    try_again = input("Do you want to try again? yes/no: ")
    if try_again == "yes" or try_again == "y":
        clear()
        current_setter()
        main()
    elif try_again == "no" or try_again == "n":
        quit()
    else:
        print("yes or no")
        try_again()


def loose_screen():
    global letters_count
    global start_time
    global elapsed_time
    elapsed_time = time.time() - start_time
    print("You lost after", str(elapsed_time)[
          :4], "secs, using", letters_count, "letters...")
    try_again()


def current_life():
    global life
    print("Remaining life: ", life)


def letter_input():
    global life
    global letters_count
    choosen_letter = input("Type in a letter: ").upper()
    if choosen_letter in used_letters:
        print("You already used this letter")
        input_situation()
    else:
        used_letters.append(choosen_letter)
        letters_count += 1
    if choosen_letter not in current_capital_upper:
        life -= 1


def word_input():
    global life
    choosen_word = input("Type in a word: ").upper()
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
    global start_time
    start_time = time.time()
    global life
    while True:
        if life > 0:
            if checker(used_letters, current_capital_upper) is True:
                win_screen()
            show_status(current_capital_upper)
            input_situation()
        else:
            loose_screen()

if __name__ == '__main__':
    used_letters = []
    life = 5
    letters_count = 0
    file_operator()
    current_setter()
    main()


"""made by Mdlkxzcmp & BDerus """
