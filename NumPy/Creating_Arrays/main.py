import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))
print('\n')

list1 = [1, 2]
print(type(list1))
arr = np.array(list1)
print(arr)
print(type(arr))
print('\n')

tuple1 = (1, 2, 3)
print(type(tuple1))
arr = np.array(tuple1)
print(arr)
print(type(arr))
print('\n')

set1 = {1, 2, 3, 4}
print(type(set1))
arr = np.array(set1)
print(set1)
print(type(arr))
print('\n')

# Dimensions in arrays

# 0-D array
arr = np.array(42)
print(arr)
print(arr.ndim) # prints the dimension of array
print('\n')

# 1-D array
arr = np.array([1, 2, 3])
print(arr)
print(arr.ndim)
print('\n')

# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)
print('\n')

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.ndim)
print('\n')

# High-Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print(arr.ndim)