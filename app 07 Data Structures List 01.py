# Data Structures

# -----------
# Lists
a = [1, 2]
b = [3, 4]
matrix = [a, b]
print(matrix)

multiplication = matrix * 2
print(multiplication)

letters = ['a', 'b', 'c', 'd']
combine = letters + a
print(combine)

combine01 = letters + matrix
print(combine01)

numbers = list(range(8))
print(numbers)

chars = list("Hello world")
print(chars)

print(len(matrix))
print(len(chars))


# ----------------
# Acessing Items
tomato = list("TOMATO")
print(tomato[2:6])
print(tomato)
tomato[0] = 'p'
tomato[2] = 't'
print(tomato)

even_step = list(range(20))
print(even_step[::2])

# ---------------
# List Unpacking

numbers02 = [1, 2, 3, 4, 5, 6, 7]
first, second, *other = numbers02
print(first, second)
print(other)


# -----------------
# Looping over lists

alphabet = list("abcdefghijklmnoprrstuvwxyz")
print(len(alphabet))
for letter in enumerate(alphabet):
    print(letter)

items = (0, "a")
index, letter01 = items
print(index)
print(letter01)


# -----------------
# Adding and Removing items

fourletters = list("abcd")
print(fourletters)
# **Add
fourletters.append("e")
print(fourletters)
# **Insert
fourletters.insert(2, "!!")
print(fourletters)
# **Remove_Last
fourletters.pop()
print(fourletters)
# **Remove specific object first occurence only, loop to remove all
fourletters.remove("!!")
print(fourletters)
# delete multiple/range of object
del fourletters[1:3]
print(fourletters)
# clear list
fourletters.clear()
print(fourletters)


# ------------------
# Finding items list location
hello = list("Hello world")
print(hello.index("r"))
# **Value error if object does not exist
# **first check to see if object exist in list

if "j" in hello:
    print(hello.index("j"))

# **count how many times an object exist in list
print(hello.count("o"))
