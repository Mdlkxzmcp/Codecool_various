# the choice screen function that is called each time a different function ends
def choice_screen():
    """a function that asks the user which option he/she wants and then calls
    the coresponding function"""
    options = ["list,", "add,", "mark,", "archive"]
    choice = input("Please specify a command {0}: ".format(options))
    if(choice == "quit"):
        quit()
    elif(choice == "list"):
        list_function()
    elif(choice == "add"):
        add_to_list()
    elif(choice == "mark"):
        mark()
    elif(choice == "archive"):
        archive()
    else:
        print("I'll add this option to my list!")
        choice_screen()


def list_function():
    """function that prints out the main_list if it exists"""
    if main_list:
        print("You saved the following to-do items: ")
        i = 0
        for entry in main_list:
            # To do: make the list show without any unneeded symbols :<
            print(str(i) + ": ", str(entry)[1:-1])
            i += 1
    else:
        print("List? What list?")

    choice_screen()


def add_to_list():
    """function that adds the users input to the main_list"""
    new_item = ["[ ] ", input("Add an item: ")]
    main_list.append(new_item)
    print("Item added.")
    choice_screen()


def mark():
    """function that marks the choosen item from the main_list"""
    if main_list:
        print("You saved the following to-do items: ")
        i = 0
        for entry in main_list:
            print(str(i) + ": ", str(entry)[1:-1])
            i += 1
        marking = int(input("Which one you want to mark as completed: "))
        main_list[marking][0] = "[x] "
        print(main_list[marking][1] + " is completed")
        choice_screen()
    else:
        print("There's nothing to mark Mark")
        choice_screen()


def archive():
    """function that erases marked items from the main_list"""
    if main_list:
        i = 0
        for entry in main_list:
            if main_list[i][0] == "[x] ":
                main_list.pop(i)
                # if an item is marked then pop gets rid of it
            i += 1
        print("All completed tasks were terminated for good.")
    else:
        print("Archive is a great band")
    choice_screen()


def main():
    global main_list
    main_list = []
    choice_screen()

if __name__ == '__main__':
    main()
