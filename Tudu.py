def list_function():
    """function that prints out the the_list if it exists or calls the
    add_to_list function to start one"""
    if the_list:
        print("You saved the following to-do items: ")
        for i, entry in enumerate(the_list, 1):
            print(i, ". ", the_list[i - 1], sep='')
    else:
        print("List? Let's start one!")
        add_to_list()


def add_to_list():
    """function that adds new items to the the_list"""
    the_list.append("[ ] " + input("Add an item: "))


def mark():
    """function that marks the choosen item from the the_list"""
    if the_list:
        list_function()
        try:
            mark = int(input("Which one do you want to mark as completed: "))
            the_list[mark - 1] = the_list[mark - 1].replace("[ ]", "[x]", 1)
            # the last bit makes the replace function happen once for a line
            print(str(the_list[mark - 1])[4:], " is completed")
        except:
            print("Can't do, sorry~")
    else:
        print("There's nothing to mark Mark")


def archive():
    """function that erases marked items from the the_list"""
    if the_list:
        for i in the_list[::-1]:
            if i[:3] == "[x]":
                the_list.remove(i)
        print("All completed tasks got deleted.")
    else:
        print("Archive is a great band")


def close():
    """function that closes the program"""
    with open("the_list.txt", "w+") as list:
        for item in the_list:
            list.write(str(item) + "\n")
    quit()


def main():
    while True:
        options = ("list,", "add,", "mark,", "archive")
        choice = input("Please specify a command {0}: ".format(options))
        if (choice == "list"):
            list_function()
        elif (choice == "add"):
            add_to_list()
        elif (choice == "mark"):
            mark()
        elif (choice == "archive"):
            archive()
        elif (choice == "x"):
            close()
        else:
            print("I'll add this option to my list!")

if __name__ == '__main__':
    # the program first tries to open the file containing the_list
    try:
        with open("the_list.txt", "r+") as list:
            the_list = list.read().splitlines()
    # if it fails it makes a new one! Then  the main() is called
    except:
        with open("the_list.txt", "a+") as list:
            the_list = list.read().splitlines()
    main()
