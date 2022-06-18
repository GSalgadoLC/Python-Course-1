from abc import ABC, abstractmethod
print()
print("Multi level inheritnace")

# Too much of a good thing is a bad thing


class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("I can fly")


class Chicken(Bird, Animal):
    pass

# A chicken cannot fly

# An employee is a person which is a living creature which is a thing
# You should limit inheritance to one or two levels


print()
print("Multiple Inheritance")


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Hi person")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# In this case both subclasses have a greet method but the manager.greet call wil call upon first instance of greet and terminate after execution
# This is brittle if someone changes subclass order in object class Manager


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass

# A flying fish can both fly and swim


print()
print("A good example of inheritance")


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError
            print("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.closed:
            raise InvalidOperationError
            print("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")


print()
print("Abstract base classes")


class MemoryStream(Stream):
    pass


stream = MemoryStream()


# Will continue with previous example

stream = Stream()
stream.open()

# Now we cannot create and instance of them which is what we wanted
# We should always subclass and not be able to call upon stream because it is unknown what type of stream we are calling

# Using a abstract base class we can provide common code to its derivatives

# Imported library abc to use functions named in line 1
