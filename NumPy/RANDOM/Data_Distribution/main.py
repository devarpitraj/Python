import numpy as np
from numpy import random

# generate array containing 100 values where the values are from [3, 5, 7, 9] with defined probabilities

arr = np.array([3, 5, 7, 9])
prob = np.array([0.1, 0.3, 0.5, 0.1])

x = random.choice(arr, p=prob, size=(100))
print(x)

x = random.choice(arr, p=prob, size=(10, 20))
print(x)