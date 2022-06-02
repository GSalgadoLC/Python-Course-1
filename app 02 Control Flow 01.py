# Control Flow


# -----------------
# Comparison Operators

from operator import truediv
from pickle import FALSE
from xmlrpc.client import boolean

x = 1
y = 2

comparison = boolean(x > y)
print(comparison)


# -------------------
# Conditional Statements

temp = input("What temperature farenheit is it: ")
conver_temp = int(temp)

if conver_temp > 75:
    print("It is hot, drink water")
elif conver_temp == 75:
    print("It is 75 deg and perfect weather")
else:
    print("It is chilly")


# ----------------------
# Ternary Operator
print(" Example 1")
age = 22
if age > + 18:
    print("Eligible")
else:
    print(" Not eligible")

print(" Example 2")
age2 = 17
message = "Eligible" if age2 >= 18 else "Not eligible"
print(message)
# Both are equivalent scripts the latter is called ternary

# -------------
# Logical Operators And Or Not
print(" Example 3")
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
print(" Example 4")
student = True
if not student:
    print("Eligible")
else:
    print("Not eligible")

# -------------
# Short Circuit Evaluation
print("Example 5")

high_salary = FALSE
good_credit_score = True

if high_salary and good_credit_score and not student:
    print("Eligible - And, And Not")

print("Example 6")
high_salary = FALSE
good_credit_score = True

if high_salary or good_credit_score or not student:
    print("Eligible - Or, Or Not")
