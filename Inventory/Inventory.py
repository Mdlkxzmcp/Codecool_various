import csv
import time

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def import_inventory(inventory, filename):
    """imports a given csv file and writes its items to the inventory
    dictionary"""

    with open(filename) as csv_inventory:
        csv_inv = csv.reader(csv_inventory, quotechar=",")
        next(csv_inv)
        for key, value in dict(csv_inv).items():
            if key in inventory:
                inventory[key] = int(value)
            elif key not in inventory:
                inventory.setdefault(key, int(value))
            else:
                print("woot woot send help")
        print("Import sucessful :>")
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
    print("Loot was added :3")
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

    print("\nInventory:")
    print("{:>7}{:>{}}".format("count", "item name", longest_val + 1))
    print(formula_for_the_line)
    # -------------------------  is made by the formula_for_the_line
    for key, value in sorted(inventory.items(),
                             key=lambda val: val[1], reverse=sort):
        print("{:{}d} {:>{}}".format(value, count_width - 1, key, longest_val))
        total_number_of_items += value
    # ------------------------- same here
    print(formula_for_the_line)
    print("Total number of items: {}".format(total_number_of_items))


def export_inventory(inventory, filename):
    """exports the inventory to a given csv file, if it doesn't exist then
    it gets created"""

    with open(filename, "w") as csv_inventory:
        writer = csv.writer(csv_inventory)
        writer.writerow(('item_name', 'count'))
        for key, value in inventory.items():
            writer.writerow([key, value])
    print("Inventory sucessfuly exported!")


def help():
    print("""
Here's what you can do here:\n
'import' an inventory from a file,
'add' some premade loot to the inventory,
'print' the inventory in order of your choice,
'display' it without any fireworks,
'export' the inventory to a file,
'help' will show this once again,
and once you're done you can type 'quit' to exit. ;>
Oh and btw, type using lowercase letters for perfect experience""")


def main():
    print("\n        Welcome to The Inventory!\n")
    help()
    while True:
        choice = input("\n\nSo what will it be?: ").lower()
        print("\n")
        if choice in ("import", "i", "imp"):
            import_inventory(inv, "import_inventory.csv")
        elif choice in ("add", "a"):
            add_to_inventory(inv, loot)
        elif choice in ("print", "p"):
            order = input("Do you want 'descending' order or 'ascending'?: ")
            if order in ("descending", "desc", "d"):
                print_order = "count,desc"
            elif order in ("ascending", "asc", "a"):
                print_order = "count,asc"
            else:
                print("This isn't a valid order. :< Setting order to default.")
                print_order = "count,desc"
            print_table(inv, print_order)
        elif choice in ("display", "dis", "d"):
            display_inventory(inv)
        elif choice in ("export", "exp", "e"):
            export_inventory(inv, "import_inventory.csv")
        elif choice in ("help", "h", "halp"):
            help()
        elif choice in ("quit", "exit", "q"):
            return False
        else:
            print("This isn't a valid option, try again~")
        time.sleep(1.2)

if __name__ == '__main__':
    main()
