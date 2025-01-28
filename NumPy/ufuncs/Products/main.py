import numpy as np

arr = np.array([1, 2, 3])

x = np.prod(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])
print(x)

# product over an axis
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)

# cumulative product
arr = np.array([1, 2, 3, 4])

newarr = np.cumprod(arr)
print(newarr)