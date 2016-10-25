# the idea is to first open all doors and then change the state of them at
# an increasing interval until it is equal to the number of doors


def doors(number_of_doors):
    """function that creates a given number of doors, then changes their state
    at an increasing interval until it is equal to the number of doors """
    doorz = [False] * number_of_doors
    # at first the state of all doors can be represented as "False" for closed
    for i in range(number_of_doors):
        for j in range(i, number_of_doors, i + 1):
            # this sets the doors to one of the two states
            doorz[j] = not doorz[j]

    print("The following doors are open: ", end="")

    # adding an index value to doorz so that the number of the door is shown
    for index, state_of_door in enumerate(doorz):
        if state_of_door:
            print(format(index + 1) + " ", end="")

# calling the function and inputing the number of doors to process
doors(100)
