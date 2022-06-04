# -------------------------
# Dictionaries
from sys import getsizeof
print()
print("Dictionaries")

point = {}
point1 = {"x": 1, "y": 2}
list()
tuple()
set()
dict()
point = dict(x=1, y=2)
# **Key word argumenets
print(point["x"])
print(point1)
point["z"] = 7
if "a" in point:
    print(point["a"])
print(point.get("a", 0))

del point["y"]
print(point)


for key in point:
    print(key, point[key])


# -------------------------
# Dictionary Comprehesion
print()
print("Dictionary Comprehension")

# ** Method 1. Atrribute error if using dict instad of list
values = []
for x in range(5):
    values.append(x*2)
print(values)


# ** Method 2
values1 = {x*2 for x in range(5)}
print(values1)


# -------------------------
# Generatpr Expressions
print()
print("Generator Expressions")

values2 = (x*2 for x in range(5))
print(values2)
# ** Expecta tuple but results in generator expression
# ** A generator expression is for many memory efficiency. Iterable, generates new value per iteration

values3 = (x * 2 for x in range(10))
print(values3)
for x in values3:
    print(x)

values5 = (x * 2 for x in range(100000))
print(getsizeof(values5))


# ------------------------------
# Unpacking Operator
print()
print("Unpackiing Operator")
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
print(*numbers)
# ** The * can unpack any iterable
print(*range(10))

# **
first = [1, 2]
second = [3, 4]
values7 = [*first, "Hello",  *second]
print(values7)
