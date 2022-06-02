from cgi import print_form
from re import A
import math


print("Hello World")

integers = 3
floats = 9.99
is_true = False
is_string = "This is a string"
print(integers, floats, is_true, is_string)

print(len(is_string))

print(is_string[0:3])

# Comment

new_line = "This will be \non two lines"
print(new_line)

first = "Tony"
last = "Stark"
full = f"{first} {last}"
print(full)

print(is_string.upper())

print(is_string.find("a"))
print(is_string.replace("a", "A"))

print("a" in is_string)
print("in" not in is_string)

x = 1
y = 2.5
xx = 1 + 3j


print(x)
print(x + x)
print(xx + xx)
print(x - y)
print(x * y)
print(x / y)
print(12 // y)
print(12 % y)
print(2**5)


print(round(3.7))
print(abs(-18))

print(math.cos(45))


x = input("Your age: ")

print(type(x))

y = int(x) + 1
print(y)
print(type(y))


print(f"x:{x}, y:{y}")
