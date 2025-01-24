import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# arr[start:end] - end index not included
print(arr[1:5])
print(arr[:5])
print(arr[1:])
print(arr[:])

# negative indexing
print(arr[-5:-2])

# step value - arr[start:end:step]
print(arr[1:5:2])
print(arr[::3])

# slicing 2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# syntax - arr[index of element, slicing index]
print(arr[1, 1:4])  # print sliced array of 1st element
print(arr[0:2, 3])  # print 3rd index element from 0 and 1st element
print(arr[0:2, 1:]) # print sliced array from both elements