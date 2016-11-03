inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    total_number_of_items = 0
    print("Inventory:")
    for key, value in inventory.items():
        print("{} {}".format(value, key))
        total_number_of_items += value
    print("Total number of items: {}".format(total_number_of_items))


def add_to_inventory(inventory, items):
    new_items = (dict((item, items.count(item)) for item in set(items)))
    iterations = 0
    while iterations < len(new_items):
        try:
            for key, value in new_items.items():
                if key in inventory:
                    inventory[key] += value
                    iterations += 1
                else:
                    inventory.setdefault(key, value)
                    iterations += 1
        except KeyError:
            print("woot woot send help")
    return inventory


def print_table(inventory, order):
    total_number_of_items = 0
    count_width = 8
    longest_val = max(len(key) for key in inventory) + 1
    formula_for_the_line = (longest_val + count_width + longest_val % 2)
    print("Inventory:")
    print("{:>7}{:>{}}".format("count", "item name", longest_val + 1))
    print("-" * formula_for_the_line)
    for key, value in inventory.items():
        print("{:{}d} {:>{}}".format(value, count_width - 1, key, longest_val))
        total_number_of_items += value
    print("-" * formula_for_the_line)
    print("Total number of items: {}".format(total_number_of_items))

add_to_inventory(inv, loot)
print_table(inv, "count,desc")
