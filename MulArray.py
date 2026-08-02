from numpy import *

# Zero Dimensional array
zero = array(10)
print(zero)

print('\n')
# One Dimensional array 
one = array([1, 2, 3, 4, 5])
print(one)

print('\n')
# Two Dimensional array
two = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two)

print('\n')    
# Three Dimensional array
three = array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(three)

# it should be homogeneous, i.e. all elements should be of the same data type. If we try to create an array with mixed data types, NumPy will upcast the data type to a common type that can accommodate all the elements.
