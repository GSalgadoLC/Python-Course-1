# -----------------------------------Private Members
print()
print("Private Members")


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

# To make item self.tags inaccessible use a self.__tag double underscore and are considered private. Not security a warning

# If you use __dict__ it will still appear and be accessible


print()
print("Properties")


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
print(product.price)

product.set_price
# UN PYTHONIC = it is not using pythons best practices

# A property is an object that sits in front of an attribute and allows to get or set value of such attribute

# Can also use a decorator above class method such as @property


print()
print("Inheritance")


# This animal class automatically inherits a base class called Object. To make it clearer we can write class Animal(Object): for demonstration purposes
class Animal(object):
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# Inheritance to avoid DRY

m = Mammal()
m.eat()
print(m.age)


print()
print("The object class")

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

o = object()

print(issubclass(Animal, Mammal))
print(issubclass(Mammal, Animal))


print()
print("Method Overriding")
# Jump back into line 62

print(m.age)
print(m.weight)

# This becomes an error because the weight class defined in mammal overrode the age class in Animal
# Animal and Mammal constructor using super() has fixed it. You can rearrange the calls if you want weight and super that is
