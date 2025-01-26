import numpy as np
from numpy import random

# shuffling arrays
# changes in-place
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# permutation
# creates a new array
arr = np.array([1, 2, 3, 4, 5])
per_arr = random.permutation(arr)
print(arr)
print(per_arr)