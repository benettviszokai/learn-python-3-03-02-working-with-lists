inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# List length - len()
inventory_len = len(inventory)

# First element in a list
first = inventory[0]

# Last element in a list
last = inventory[-1]

# Slicing - index 2 to index 6 (not including)
inventory_2_6 = inventory[2:6]

# Slicing - first 3 items
first_3 = inventory[:3]

# Counting items - How many twin beds?
twin_beds = inventory.count("twin bed")

# Removing items with indexes -> 5th item -> 4th index
removed_item = inventory.pop(4)

# Inserting items with indexes (11. element, 10th index)
inventory.insert(10, "19th Century Bed Frame")

# Sorting lists
inventory.sort() # This sorts the original list -> no return value
new_inventory = sorted(inventory) # This returns a new list, the original will be unchanged

print(inventory)
print(new_inventory)
