import numpy as np
from numpy import random

# generate a random integer from 0 t0 50
x = random.randint(50)
print(x)

# generate a random float from 0 to 1
x = random.rand()
print(x)

# generate a random float from a to b
# x = a + (b - a) * random.rand()
# generate a random float between 5 to 11
x = 5 + 6 * random.rand()
print(x)

# generate random arrays

# integers
# specify the shape of array in size parameter

# 1D
x = random.randint(100, size=(5))
print(x)

# 2D
x = random.randint(50, size=(3, 5))
print(x)

# floats
# specify the shape of array in rand()

# 1D
x = 9 + 2 * random.rand(4)
print(x)

# 2D
x = random.rand(3, 6)
print(x)

# generate random no. from arrays
x = random.choice([3, 5, 7, 9])
print(x)

arr = np.array([4, 8, 10, 1, 0])

# 1D
x = random.choice(arr, size=(3))
print(x)

# 2D
x = random.choice(arr, size=(3, 2))
print(x)