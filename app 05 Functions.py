# -------------------
# Defining Functions
def greet():
    print("Hi there")
    print("Welcome Aboard")


greet()

# -----------------
# Arguments


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


greet("Tony", "Stark")

# --------------
# Types of Functions


def greet(name):
    print(f"Hii {name}")


def get_greeting(name):
    return f"Hi {name} "


message = get_greeting("Tony")
file = open("content.txt", "w")
file.write(message)

# ----------------
# Key word arguments


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)


print(increment(7, by=3))

# --------------
# XArgs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(7, 15, 8, 6))


# ----------------
# XXArgs

def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Tony", age=23)


# ---------------
# Scope
banana = "global_variable"
print(banana)


def greet(name):
    print(name)
    message = "a"
    global banana
    banana = "changed the global variable value"
    print(banana)


greet(1)


def send_email(name):
    message = "b"


# ----------------------
# Debugging

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3, 4, 5, 6, 7))
