import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

# Addition
newarr = np.add(arr1, arr2)
print('Addition -', newarr)

# Summation
newarr = np.sum([arr1, arr2])
print('Summation -', newarr)

# summation over an axis
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

# cumulative sum or partial sum
arr = np.array([1, 2, 3, 4, 5])

newarr = np.cumsum(arr)
print(newarr)