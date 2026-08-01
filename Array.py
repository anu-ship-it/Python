from array import *

# For Integer array
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# For Float array
val2 = array('d', [1, 2, 3, 11.5])

# For Character array
val3 = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(val)
print(val2)
print(val3)


# Normal for loop
for i in range(0,5):
    print(val[i], end=' ')

print('\n')    

# Inhanced for loop 
# Here we  don't need to give range and index, we can directly access the values of array
for x in val:
    print(x, end=',')

print('\n')

# Using len
for i in range(0,len(val2)):
    print(val2[i], end=' ')

print('\n')

# When we wanted to know the typecode of our array
print(val.typecode) 
print(val2.typecode)    
print(val3.typecode)    

print('\n')

# When we wanted to reverse the array
val.reverse() # First we need to reverse the array and then we can print it 
for x in val:
    print(x, end=' ')

# When we wanted to add a new element in array
print('\n')
val.insert(2,15) # It will add 15 in 2nd index of array and shift the rest of the elements to right
val.append(20) # It will add 20 at the end of array
val[3] = 25 # It will replace or override the value at 3rd index with 25

# When we wanted to create a copyarray of our array
print('\n')
copyarray = array(val2.typecode, (x*4 for x in val2)) # It will create a copy of val2 array

for i in range(0,len(copyarray)):
    print(copyarray[i], end=' ')

# When we wanted to remove an element from array
print('\n')
val.pop(2) # It will remove the element at 2nd index of array
val.pop() # It will remove the last element of array
val.remove(25) # It will remove the first occurrence of 25 from array


# Slicing 
# When we want to slice an array
print('\n')
sliced_array = val[2:5] # It will create a slice of array from 2nd to 4th index
for x in sliced_array:
    print(x, end=' ')

# When we wanted to slice an array where we don't want the end 2 elements of array
print('\n')
sliced_array2 = val[1:3] # It will create a slice of array from 1st to 2nd index
for x in sliced_array2:
    print(x, end=' ')

# When we wanted to reverse the sliced array
print('\n')
sliarr = val[::-1] # It will create a slice of array from last to first index
for x in sliarr:
    print(x, end=' ')

    