import numpy as np

# print data type using 'dtype'
arr = np.array([1, 2, 3])
print(arr.dtype)

arr = np.array(['a', 'b', 'c'])
print(arr.dtype)

arr = np.array(['A', 'B', 'C'])
print(arr.dtype)

arr = np.array(['Apple', 'banana'])
print(arr.dtype)

arr = np.array(['a', 'B'])
print(arr.dtype)

# creating arrays with defined data types
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# fir 'i', 'u', 'f', 'S' and 'U' we can define sizes also
arr = np.array([1, 2, 3], dtype='i8')
print(arr)
print(arr.dtype)

# arr = np.array(['a', '1'], dtype='i') # ValueError is raised - ValueError: invalid literal for int() with base 10: 'a'

# converting data types on existing arrays
arr = np.array([1.1, 2.1, 0.7, 3.5, 0])

newarr = arr.astype('i')    # 'i' by default size is 32 bits
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)    # int by default size is 64 bits
print(newarr)
print(newarr.dtype)

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)