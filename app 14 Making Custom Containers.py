# ---------------------------------------------------Arithmetic Operations
print()
print("Arithmetic Operations")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y+other.y)


var1 = Point(10, 20)
var2 = Point(3, 4)
combined = var1 + var2
print(combined.x)
print(combined.y)


# ---------------------------------------------------Making Custom Containers
print()
print("Making Custom Containers")


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)

# A typical dictionary would create to items a upper case python and a lower case python
print("The number of occurences of the tag 'python' is ")
print(cloud["python"])

# We can set the occurences directly with next method
cloud["python"] = 10
print(len(cloud["python"]))
