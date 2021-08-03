"""Write a function that accepts any possible 'inventory' dictionary and
displays it in prettified format"""

ascent_char_inv = {'shotgun ammo': 45,
                   'handgun ammo': 125, 'energy': 80,
                   'augmentation': 2}

looted_items = ['shotgun ammo', 'shotgun ammo',
                'shotgun ammo', 'shotgun ammo',
                'shotgun ammo', 'augmentation',
                'flame-resistant leggings']


def display_inventory(inventory):
    item_total = 0
    for k, v in inventory.items():
        print(f"\n{k.title()}: {v}")
        item_total += v
    return item_total


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# Run 'add_to_inventory' first, so that additional loot gets calculated
inv = add_to_inventory(ascent_char_inv, looted_items)
print("\n***INVENTORY***")
# print(f"- Shotgun Ammo\t {str(ascent_char_inv['shotgun ammo'])}")
# print(f"- Handgun Ammo\t {str(ascent_char_inv['handgun ammo'])}")
# print(f"- Energy\t {str(ascent_char_inv['energy'])}")
# print(f"- Augmentation\t {str(ascent_char_inv['augmentation'])}")
print(f"\nTOTAL NUMBER OF ITEMS => {display_inventory(inv)}")
