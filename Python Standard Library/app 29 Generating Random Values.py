import random
import string

print(random.random())
print(random.randint(1, 10))

print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9], k=3))


print("".join(random.choices(string.ascii_letters, k=10)))

print(string.ascii_letters)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(numbers)
print(numbers)
