import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.concatenate((a1, a2), axis=1)  
print(arr)

arr = np.concatenate((a1, a2), axis=0)  
print(arr)

# using stack() function
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# stacking along rows
arr = np.hstack((arr1, arr2))
print(arr)

# stacking along columns
arr = np.vstack((arr1, arr2))
print(arr)

# stacking along height/depth
arr = np.dstack((arr1, arr2))
print(arr)