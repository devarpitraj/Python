import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

print(np.log10(arr))

print(np.log(arr))

# custom log using math.log() and np.frompyfunc()
import math

nplog = np.frompyfunc(math.log, 2, 1)

# log of 100 base 15
print(nplog(100, 15))