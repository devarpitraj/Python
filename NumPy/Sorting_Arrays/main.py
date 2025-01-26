import numpy as np

# 1D array
arr = np.array([3, 0, 19, 2, 9, -1])
s = np.sort(arr)
print(s)

# strings
arr = np.array(['b', 'c', 'a'])
print(np.sort(arr))

# boolean
arr = np.array([True, False, True])
print(np.sort(arr))

# 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))