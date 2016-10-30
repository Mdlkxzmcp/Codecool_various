import random
import time
import datetime

global current_capital


def clear():
    """sets counter, used_letters and life to starting values"""
    global life
    global used_letters
    global counter
    counter = 0
    used_letters = []
    life = 5


def file_operator():
    """opens up the countries_and_capitals.txt file and transforms it into a
    usable list after which the file is closed"""
    global countries_and_capitals
    with open("countries_and_capitals.txt") as list:
        countries_and_capitals = list.read().splitlines()


def current_setter():
    """takes a pair from the countries_and_capitals list and then separates
    them into two seperate variables ( + creates the current_capital_upper)"""
    global countries_and_capitals
    global current_capital
    global current_capital_upper
    global current_country
    choosen_pair = random.choice(countries_and_capitals)
    current_capital = choosen_pair.split("| ")[1]
    current_capital_upper = current_capital.upper()
    current_country = choosen_pair.split(" |")[0]


def start_screen():
    print("\n            Welcome to Teh Hungoverman Gaem\n"
          "\nYou wake up, surrounded by "
          "alien grounds you realize that your head hurts like a mofo.\n"
          "Stored deep in your memory is the name of a capital that holds the "
          "key to realizing where you are.\nYou gotta hurry though, you feel "
          "like this memory is about to fade out!!!\n")


def checker(current_capital_upper):
    global used_letters
    """checker(list, string) checks if values from list are all present in
    the string and then returns a boolean"""
    used_letters.append(" ")
    state = set(current_capital_upper).issubset(used_letters)
    used_letters.remove(" ")
    return state


def input_situation():
    choice = input("Do you want to try a (l)etter or a (w)ord?: ")
    if choice == "letter" or choice == "l":
        letter_input()
    elif choice == "word" or choice == "w":
        word_input()
    else:
        print("Wait what?")
        input_situation()


def letter_input():
    global life
    global counter
    choosen_letter = input("Type in a letter: ").upper()
    if len(choosen_letter) == 1 and choosen_letter.isalpha():
        counter += 1
        if choosen_letter in used_letters:
            print("You already used this letter")
            letter_input()
        else:
            used_letters.append(choosen_letter)
        if choosen_letter not in current_capital_upper:
            life -= 1
    else:
        print("letters brain, letters, please!")
        letter_input()


def word_input():
    global life
    global counter
    choosen_word = input("Type in a word: ").upper()
    if len(choosen_word) > 2:
        counter += 1
        if choosen_word == current_capital_upper:
            win_screen()
        else:
            life -= 2
    else:
        print("Wait.. No, what? Ok, one more time...")
        word_input()


def show_status():
    """prints out "_ " or the letter itself from the current_capital_upper if
    it is in the used_letters list"""
    global current_capital_upper
    global current_country
    global used_letters
    global life
    current_life()
    if life == 1:
        print("\nOh! It's the capital of %s\n!" % current_country)
    print("? ", end="")
    for letter in current_capital_upper:
        if letter == " ":
            print("  ", end="")
        elif letter in used_letters:
            print(letter, end="")
        else:
            print(" _", end="")
    print("  ?\n")
    if used_letters:
        print("  You already tried: ", used_letters)


def current_life():
    """shows remaining life"""
    global life
    print("Remaining tries before you forget: ", life)


def win_screen():
    """the "screen" that is displayed when the game is won. Measures the time
    spent and shows the counter plus the time of course. Calles the
    high_score_handler function after which it calls the try_again screen"""
    global counter
    global current_capital
    global start_time
    global usable_elapsed_time
    elapsed_time = time.time() - start_time
    usable_elapsed_time = str(int(round(elapsed_time)))
    print("\n\nCongratulations! You remembered after", counter,
          "tries in", usable_elapsed_time, "secs, nice!\n"
          "Last night was indeed crazy, you better call your wife... o.o")
    high_score_handler()
    try_again()


def loose_screen():
    """the screen that is displayed when the user looses. Shows elapsed time
    and calls the try again function"""
    global counter
    global start_time
    global elapsed_time
    elapsed_time = time.time() - start_time
    print("\nYou forgot and are now lost for good. "
          "It took you {} secs and {} guesses to finally forget...".format(str(elapsed_time)[:4], counter))
    try_again()


def try_again():
    """asks if the user wants to try / play again and depending on the decision
    either starts a new game by calling clear, current_setter & main
    functions or quits the program"""
    global life
    print("")
    high_score_screen()
    try_again = input("\nDo you want to play again? yes/no: ")
    if try_again == "yes" or try_again == "y":
        clear()
        current_setter()
        main()
    elif try_again == "no" or try_again == "n":
        quit()
    else:
        print("yes or no")
        try_again()


def high_score_handler():
    """asks the user for his name if he won after which it stores the new high
    score to the high_scores.txt file"""
    global usable_elapsed_time
    player_name = input("Type in your name to add it to the high scores!: ")
    day = datetime.datetime.now()
    new_high_score = [player_name, " | ", day.strftime(
        "%Y-%m-%d"), " | ", usable_elapsed_time, " | ", str(counter), " | ",
        current_capital, "\n"]
    print("".join(new_high_score))
    with open("high_scores.txt", "a+") as high_scores:
        high_scores.writelines(new_high_score)


def high_score_screen():
    """displays the current high scores!"""
    global high_scores
    with open("high_scores.txt") as list:
        high_scores = list.read().splitlines()
        print("\n".join(high_scores))


def main():
    global start_time
    start_screen()
    # ready... set... go!!!
    start_time = time.time()
    global life
    while True:
        if life > 0:
            # this calles the win screen if the user guessed the word :>
            if checker(current_capital_upper) is True:
                win_screen()
            show_status()
            input_situation()
        else:
            # or the loose screen if the user lost :<<<
            loose_screen()

# this first prepares the game and then calles the main that starts it
if __name__ == '__main__':
    clear()
    file_operator()
    current_setter()
    main()


"""made by Mdlkxzcmp & BDerus aka Maximiliaan Strother III & Bartek Deruś"""
