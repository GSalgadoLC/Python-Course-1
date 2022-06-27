# NumpPy Heavily used in scientific computations like data science and machine learning
# NumPy brings in superfact non dimensional arrays that takes less memory than built in lists


from turtle import setworldcoordinates
import numpy as np

array = np.array([[1, 2, 3],    [4, 5, 6], [7, 8, 9]])
print(array)
print(type(array))

print()
print("This is a matrix 0_0")
print()
print(array.shape)

print()
array2 = np.zeros((4, 5), dtype=int)
print(array2)


print()
array3 = np.ones((4, 5), dtype=int)
print(array3)


print()
array3 = np.full((4, 5), 5,  dtype=int)
print(array3)


print()
array4 = np.random.random((4, 5))
print(array4)

print()
print("....")
print(array4[0, 0])


print()
array5 = np.random.random((4, 5))
print(array5)

print()

print(array4 > array5)

print()

print(array5[array4 > 0.2])

print()
print(np.sum(array4))


print()
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first+second)


print()
print(first * 5)

print(first + 5)

print()
dimensions_inch = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)


print()
# This is implementaion in pure python to convert
dimensions_inch = [1, 2, 3, 4, 5]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
