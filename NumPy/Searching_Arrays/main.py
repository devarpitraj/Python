import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

x = np.where(arr == 4)
print(x)

x = np.where(arr % 2 == 0)
print(x)

x = np.where(arr % 2 == 1)
print(x)

# binary search - searchsorted()
# applied on sorted arrays

x = np.searchsorted(arr, 3)
print(x)

# search from right
x = np.searchsorted(arr, 3, side='right')
print(x)

# multiple values search

x = np.searchsorted(arr, [2, 0, 3, 11, 10, -3])
print(x)