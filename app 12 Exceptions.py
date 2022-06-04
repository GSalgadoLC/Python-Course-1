# ----------
# Exceptions

from timeit import timeit
from site import addsitepackages


print()
print("Exceptions")

numbers = [1, 2, 3, 4, 5, 6, 7]
# Error index out of range
# print(numbers[8])

age = int(input("Age: "))
# A letter character will crash application, Value Error

# -------------------
# Handling Exceptions
print()
print("Handling Exceptions")

try:
    years = int(input("Years: "))
except ValueError as error_exception:
    print("You did not enter a vald age")
    print(error_exception)
    print(type(error_exception))
else:
    print("No exceptions were thrown")
print("Execution Continues")


# -------------------
# Handling Different Exceptions
print()
print("Handling Differnet Exceptions")


try:
    random = int(input("Enter a number: "))
    xfactor = 10 / random
except ValueError:
    print("You did not enter a number")
except ZeroDivisionError:
    print("Number cannot be zero")
else:
    print("No exceptions were found")


# -------------------
# Cleaning Up
print()
print("Cleaning Up")


try:
    numero = int(input("Enter a numero"))
    file = open("app.py")
    zdiv = 100 / numero
except(ValueError, ZeroDivisionError):
    print("You did not enter a valid number")
else:
    print("No exceptions were resulted")
finally:
    file.close()


# -------------------
# The with statement
print()
print("The with statement")

try:
    numero2 = int(input("Enter a numero"))
    with open("app.py") as file2:
        print("File opem, read write")
    zdiv1 = 100 / numero2
except(ValueError, ZeroDivisionError):
    print("You did not enter a valid number")
else:
    print("No exceptions were resulted")
finally:
    file2.close()

# ** With the with call python will automatically release external resources


# -------------------
# Raising Exceptions
print()
print("Raising Exceptions")


def calculate_xfactor(edad):
    if edad <= 0:
        raise ValueError("Edad cannot be zero or less")
    return 10 / edad


try:
    calculate_xfactor(-7)
except ValueError as error:
    print(error)


# -------------------
# Cost of Raising Exceptions
print()
print("Cost of Raising Exceptions")

code1 = """
def calculate_xfactor(edad):
    if edad <= 0:
        raise ValueError("Edad cannot be zero or less")
    return 10 / edad


try:
    calculate_xfactor(-7)
except ValueError as error:
    print(error)

"""
print("firse code=", timeit(code1, number=100))


code2 = """
def calculate_xfactor(edad):
    if edad <= 0:
        return None
    return 10 / edad

xfactor =     calculate_xfactor(-7)
if xfactor == None:
    pass

"""
print("second code=", timeit(code2, number=100))
