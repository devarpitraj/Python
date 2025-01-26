import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# numpy will adjust from end if elements are less or more

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([1, 2, 3, 4, 5])
newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# splitting 2D arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# can specify the axis also
newarr = np.array_split(arr, 2, axis=1)

print(newarr)
print(newarr[0])
print(newarr[1])

# splitting along rows
newarr = np.hsplit(arr, 2)
print(newarr)
print(newarr[0])
print(newarr[1])

# splitting along cols
newarr = np.vsplit(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# splitting along depth - dsplit work on arrays of dimension 3 or more
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
newarr = np.dsplit(arr, 2)
print(newarr)
print(newarr[0])
print(newarr[1])