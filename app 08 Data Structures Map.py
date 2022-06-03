# Data Structures 02

# ------------------
# Sorting Lists
from pickle import FALSE
print()
print("Sorting Lists")


numbers = [1, 6, 3, 50, 34, 15, 23, 18, 200]
print(numbers)
# This creates separate list, does not change original variable
print(sorted(numbers))
print(numbers)
numbers.sort(reverse=False)
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 90),
    ("Product3", 30),
    ("Product4", 20),
    ("Product5", 50),
    ("Product6", 15),
    ("Product7", 70)
]

# Creting a function that sorts the tuples inside a list by their price


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# -----------------
# Lambda Functions
print()
print("Lambda Functions")

# **Using above tuples that are in list variable (items)
items.sort(key=lambda item: item[1])
print(items)


# ---------------------
# Map Functions
print()
print("Map Functions")
prices = []
for item in items:
    prices.append(item[1])

print(prices)

x = list(map(lambda item: item[1], items))
# This map function will iterate over the iterable object(items) and will call the lambda function on each of the this iterable

for item in x:
    print(item)

print(x)


# ---------------------
# Filter Functions
print()
print("Filter Functions")

shopping_cart = [
    ("product01", 27),
    ("product02", 57),
    ("product03", 17),
    ("product04", 7),
    ("product05", 12),
    ("product06", 24)
]


under20 = list(filter(lambda item: item[1] < 20, shopping_cart))
print(f"You can buy {under20}")


# -------------------------
# List Comprehensions is the same as line 60
print()
print("List Comprehension")

notunder20 = [item[1] for item in shopping_cart]


# ----------------------
# Zip Function
print()
print("Zip Functions")

list1 = [1, 2, 3]
list2 = [10, 20, 30]
goal = [(1, 10), (2, 20), (3, 30)]

print(list(zip(list1, list2)))
