def main():
    global the_list
    the_list = []
    choice_screen()


# the choice screen function that is called each time a different function ends
def choice_screen():
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
    if(len(the_list) != 0):
        print("You saved the following to-do items: ")
        i = 0
        for entry in the_list:
            # To do: make the list show without any unneeded symbols :<
            print(str(i) + ": ", str(entry)[1:-1])
            i += 1
    else:
        print("List? What list?")

    choice_screen()


def add_to_list():
    new_item = ["[ ] ", input("Add an item: ")]
    the_list.append(new_item)
    print("Item added.")
    choice_screen()


def mark():
    if(len(the_list) != 0):
        print("You saved the following to-do items: ")
        i = 0
        for entry in the_list:
            print(str(i) + ": ", str(entry)[1:-1])
            i += 1
        marking = int(input("Which one you want to mark as completed: "))
        the_list[marking][0] = "[x] "
        print(the_list[marking][1] + " is completed")
        choice_screen()
    else:
        print("There's nothing to mark Mark")
        choice_screen()


def archive():
    if(len(the_list) != 0):
        i = 0
        for entry in the_list:
            if the_list[i][0] == "[x] ":
                the_list.pop(i)
                # if an item is marked then pop gets rid of it
            i += 1
        print("All completed tasks were terminated for good.")
    else:
        print("Archive is a great band")
    choice_screen()

if __name__ == '__main__':
    main()
