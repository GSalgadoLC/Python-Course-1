def fizz_buzz(input):
    if input % 3 == 0:
        result = "Fizz"
    else:
        result = "Buzz"
    return result


print(fizz_buzz(5))


# ------------
# Implementation 2

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return"Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print("Implementation 2: Test Eval")
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
