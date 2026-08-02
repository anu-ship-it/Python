from numpy import *
# Creating an array with mixed data types
val = array([1, 2, 3, 4.5,'a'])

for x in val:
    print(x, end=' ')

print("\n")
# Creating an array using linspace
val1 = linspace(10, 20, 5)  # 5 numbers between 10 and 20

for x in val1:
    print(x, end=' ')

print("\n")
# Creating an array using arange
val2 = arange(0, 10, 2)  # Numbers from 0 to 10 with a step of 2

for x in val2:
    print(x, end=' ')

print("\n")
