import csv


def import_inventory(inventory, filename):
    """imports a given csv file and writes its items to the inventory
    dictionary"""

    with open(filename) as csv_inventory:
        csv_inv = csv.reader(csv_inventory, quotechar=",")
        next(csv_inv)
        for key, value in dict(csv_inv).items():
            if key in inventory:
                inventory[key] += int(value)
            elif key not in inventory:
                inventory.setdefault(key, int(value))
            else:
                print("woot woot send help")
        return inventory


def display_inventory(inventory):
    """displays the content of the inventory dictionary"""

    total_number_of_items = 0

    print("Inventory:")
    for key, value in inventory.items():
        print("{} {}".format(value, key))
        total_number_of_items += value
    print("Total number of items: {}".format(total_number_of_items))


def add_to_inventory(inventory, items):
    """sorts items argument so that they become a dictionary with values
    depending on the number of repetitions of a given item in the items
    argument. Then the  newly created dictionary is merged to the inventory
    argument."""

    new_items = (dict((item, items.count(item)) for item in set(items)))

    for key, value in new_items.items():
        if key in inventory:
            inventory[key] += value
        elif key not in inventory:
            inventory.setdefault(key, value)
        else:
            print("woot woot send help")

    return inventory


def print_table(inventory, order):
    """print_table prints out the inventory in a readable and sortable way"""

    total_number_of_items = 0
    count_width = 8
    longest_val = max(len(key) for key in inventory) + 1
    formula_for_the_line = "-" * (longest_val + count_width + longest_val % 2)
    # the sort variable is set here depending on the order argument
    if order == "count,desc":
        sort = True
    elif order == "count,asc":
        sort = False
    else:
        print("Not now .-.")  # if order is typed in wrong sorting is ascending
        sort = False

    print("Inventory:")
    print("{:>7}{:>{}}".format("count", "item name", longest_val + 1))
    print(formula_for_the_line)
    # ------------------------- made by the formula_for_the_line
    for key, value in sorted(inventory.items(),
                             key=lambda val: val[1], reverse=sort):
        print("{:{}d} {:>{}}".format(value, count_width - 1, key, longest_val))
        total_number_of_items += value
    # ------------------------- again made by the formula_for_the_line
    print(formula_for_the_line)
    print("Total number of items: {}".format(total_number_of_items))


def export_inventory(inventory, filename):
    print(booty)


def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    import_inventory(inv, "import_inventory.csv")
    add_to_inventory(inv, loot)
    print_table(inv, "count,desc")
    export_inventory(inv, "import_inventory.csv")

if __name__ == '__main__':
    main()
