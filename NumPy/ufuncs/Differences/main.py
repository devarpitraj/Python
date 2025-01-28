import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
print(newarr)

arr = np.array([10])
newarr = np.diff(arr)
print(newarr)

# repeat the function by using 'n' parameter
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=3)
print(newarr)