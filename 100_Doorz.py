# the idea is to first open all doors and then change the state of them at
# an increasing interval until it is equal to the number of doors


def doors(number_of_doors):
    # at first the state of all doors can be represented as "False" for closed
    doorz = [False] * number_of_doors

    for i in range(number_of_doors):
        for j in range(i, number_of_doors, i + 1):
            # this sets the doors to one of the two states
            doorz[j] = not doorz[j]

    print("The following doors are open: ", end="")

    # adding an index value to doorz so that the number of the door is shown
    for index, door in enumerate(doorz):
        if(door is True):
            print(format(index + 1) + " ", end="")

# calling the function and inputing the number of doors to process
doors(100)
