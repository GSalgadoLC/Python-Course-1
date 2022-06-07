# --------
# Classes
print()
print("Classes")
# A class is a blueprint for creating new objects
# An oject is an instance of a class
# Class is Human
# Object is Harry, Ron, Hermione and Draco

print()
print("Creating Classes")

# Uppercase class meta


# class Point:
# def draw(self):
# print("draw")


#point = Point()
# print(type(point))

#print(isinstance(point, Point))


# ---------------------------------------------------Constructors
print()
print("Constructors")


class Point:
    default_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # Decorator
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ( {self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()


# ---------------------------------------------------Class Vs Instance Attributes
print()
print("Class vs Instance Attributes")

point1 = Point(2, 3)
point1.draw()
print(point1.default_color)
# Class attribute shared across all instance among a class
print(Point.default_color)


point2 = Point(4, 3)
point2.draw()
# Line33 Default_color is a class level attribute and can be read via class reference

# Point object and point class are different.


# ---------------------------------------------------Class Vs Instance Methods
print()
print("Class vs Instance Methods")
# Creating multiple that is (0,0). IE point = Point(0,0) this is one way via instance methods

# LINE 39.  Zero is a method that is defined at the class level, factory method that creates a new object

point0 = Point.zero()
point0.draw()


# ---------------------------------------------------Magic Methods
print()
print("Magic Methods")

# Methods that have two underscores at the beginning and at the end. Called automatically by python interpreter
# LINE 43
print(point)
print(str(point))


# ---------------------------------------------------Comparing Objects
print()
print("Comparing objects")


class Compare:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > self.y and self.y > other.y


value1 = Compare(1, 2)
value2 = Compare(1, 5)
print(value1 == value2)

# The result is false because this operation compares the address in memory. IE they have distinct addresses
# Need a magic method LINE 104

print(value1 > value2)
