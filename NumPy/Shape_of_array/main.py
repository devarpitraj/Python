import numpy as np

# shape attribute returns a tuple and integer at every index represents the no. of elements present in the corresponding dimension
arr = np.array([1, 2, 3])
print(arr.shape)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)    # (2, 3) means 1st dimension has 2 elements and 2nd dimension has 3 elements

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape)

# Reshape 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3, 4)
print(newarr)
print(newarr.base)  # reshape creates a view

# 1-D to 3-D
newarr = arr.reshape(2, 3, 2)
print(newarr)

# unknown dimension - pass -1 in atmost one dimension and numpy will calculate the corresponding value for that dimension
newarr = arr.reshape(2, 1, -1)
print(newarr)

# flatting the multidimensional array to 1-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)