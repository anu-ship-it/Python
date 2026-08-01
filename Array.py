import array

# For Integer array
val = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# For Float array
val2 = array.array('d', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.5])
#print(val)


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
