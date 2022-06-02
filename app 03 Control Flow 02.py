# Control Flow Part 2

# ----------
# Chaining Comparison Operators

from tokenize import Number


age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# -------------
# For loops

for number in range(3):
    print("Send the message", number + 1, (number + 1)*'.')


# -------------
# For Else

successful = True
for number in range(3):
    print("Attempt", number+1)
    if successful:
        print("successful")
        break
else:
    print("Failed Transaction")

# --------------
# Nested Loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
# ----------
# Iterables

for x in range(7):
    print(x)
for y in "Python":
    print(y)
for z in [1, 2, 3, 4]:
    print(z)

# ----------------
# While Loops
number = 0
while number < 5:
    print(number, "is less than 5")
    number += 1

# ---------------
# Infinite Loops

while True:
    print(".")

# ---------------
# Exercise
