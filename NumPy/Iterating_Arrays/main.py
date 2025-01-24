import numpy as np

# simple iteration

# 1D array
arr = np.array([1, 2, 3])
for x in arr:
    print(x)
    
# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# this will print n-1th dimension
for x in arr:
    print(x)
    
# to get each scalar use 'n' for loops for n dimension
for x in arr:
    for y in x:
        print(y)
        
print('\n')
# Iterating using 'nditer()'

for x in np.nditer(arr):
    print(x)
    
# change datatype while iterating

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['float']):
    print(x)
# flags=['buffered'] is used as an extra space because this operation is not in-place

# iterating with different step size

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)
    
# ndenumerate() returns a tuple with index number and the value

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
    
arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)