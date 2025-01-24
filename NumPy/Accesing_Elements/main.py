import numpy as np

# 1-D array
arr = np.array([1, 2, 3, 4])
print(arr[0], arr[2])

# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 0], arr[0, 2])

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 1, 2], arr[0, 0, 0])

# Negative Indexing - access from end
arr = np.array([1, 2, 3, 4])
print(arr[-1], arr[-4])