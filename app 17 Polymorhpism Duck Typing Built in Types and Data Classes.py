from collections import namedtuple
from abc import ABC, abstractmethod
print()
print("Polymorhpism")


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbook")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
print(isinstance(ddl, UIControl))
draw(ddl)
textbox = TextBox()
draw(textbox)

# Many forms
# Draw method is taking many forms

print()
print("Duck Typing")

# If it walks and talks like a duck its probably a duck so it will be treated like a duck

print()
print("Extending Built In Types")


class Text(str):
    def duplicate(self):

        return self + self


text = Text("Python")
print(text.duplicate())

print()
print("Data Classes")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
# The result will be false because by default Python compares address of the variables

print(id(p1))
print(id(p2))

# INSTEAD OF THE CLASS POINT OBJECT WE CAN DO


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
p2 = Point(x=1, y=2)
print(p1 == p2)

# These tuples are immutable and cannot be set
