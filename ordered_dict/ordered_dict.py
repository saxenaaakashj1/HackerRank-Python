from collections import OrderedDict

# Read number of entries
n = int(input())
items = OrderedDict()

# Read item name and price, update total for each item
for _ in range(n):
    item, price = input().rsplit(" ", 1)
    items[item] = items.get(item, 0) + int(price)

# Print each item and its total price in order of appearance
for item in items:
    print(item, items[item])