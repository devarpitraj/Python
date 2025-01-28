import numpy as np

# create set
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

set1 = np.unique(arr)
print(set1)

# union

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.union1d(set1, set2)
print(newarr)

# intersection
newarr = np.intersect1d(set1, set2, assume_unique=True)
print(newarr)

# difference
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)

# symmetric difference
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)