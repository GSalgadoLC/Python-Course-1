# ----------------------
# Stacks
from array import array
from collections import deque
from re import A
from tkinter import BROWSE


print()
print("Stacks")
# **LIFO Last in, First Out

broswing_session = []
broswing_session.append(1)
broswing_session.append(2)
broswing_session.append(3)
broswing_session.append(4)
print(broswing_session)
last = broswing_session.pop()
print(last)
print(broswing_session)
print("redirect", broswing_session[-1])

# **Falsy values are 0 ' ' " " [] empty <-----

if not broswing_session:
    broswing_session[-1]


# -------------------------
# Queues
print()
print("queues")
# **First in, First Out. A list can be used but you would need to shift all of items in liest to the left
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
if not queue:
    print("Empty")


# -------------------------
# Point
print()
print("Point")

# You do not need to add () to indicate type is of tuple
point = 1, 2, 3
print(type(point))
# **You can do math on tuples
print(point[0:2])
x, y, z = point
if 10 in point:
    print("Exist")
print(point)
print(x, y, z)
# **Tuples are immutable
# **Cannot set point[0] = 10
# **We can use tuples when are we prventing accidental changes that can happen such as in List

# -------------------------
# Swapping Variables
print()
print("Swapping Variables")
x = 10
y = 11

temp = x
x = y
y = temp


print(f"This is X:", x)
print(f"This is Y:", y)
# ** alternative method
a = 7
b = 5
print("a", a)
print("b", b)
a, b = b, a
print("a", a)
print("b", b)


# -------------------------
# Arrays
print()
print("Arrays")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# **Arrays can be faster and more efficient, performance wise
numbers = array("i", list)
numbers.append(0)
print(numbers)
print(type(numbers))
# **Unlike lists the objects in this array are TYPE
# ** Google python array type code, must be spcifiec in this example the type is "i"


# -------------------------
# Sets
print()
print("Sets")

numeros = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 10, 6, 7, 9, 10, 19]
uniques = set(numeros)
print(numeros)
print(uniques)
# **Look at how in the termial the list variable numeros is [] but the set variable uniques is {}

second = {1, 5}
print(second)
second.add(10)
print(second)
second.remove(1)

print(second)
print(len(second))

# **Where sets shine are in the math realm of operations Union | Interscetion & Differnece - and Symmetric difference ^
print(uniques | second)
print(uniques & second)
print(uniques - second)
print(uniques ^ second)
# **Cannot access by index, must use list
# Can check for existence in set

if 19 in uniques:
    print("Yes")
