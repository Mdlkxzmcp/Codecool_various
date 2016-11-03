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
    try:
        for key, value in new_items.items():
            inventory[key] += value
    except KeyError:
        inventory.setdefault(key, value)
    print(inventory)


add_to_inventory(inv, loot)
display_inventory(inv)
