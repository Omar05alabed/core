import sys


def ft_inventory_system():
    inventory = {}
    for item in sys.argv[1]:

        if item in inventory.keys():
            inventory.update({item: inventory[item] + 1})
        else:
            inventory.update({item: 1})

    print(inventory)


ft_inventory_system()
