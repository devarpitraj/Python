import numpy as np

# LCM

x = np.lcm(6, 9)
print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

# GCD

x = np.gcd(16, 20)
print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)