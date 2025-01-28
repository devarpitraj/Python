import numpy as np
from numpy import pi

# takes input in radians
x = np.sin(pi / 2)
print(x)

x = np.cos(pi)
print(x)

x = np.tan(pi/4)
print(x)

arr = np.array([pi/2, pi, pi/4, 2*pi])
x = np.sin(arr)
print(x)
# output is [ 1.00000000e+00  1.22464680e-16  7.07106781e-01 -2.44929360e-16] which is correct but to see 1 and 0 we have round the answer

x = np.round(x, decimals=10)
print(x)

# radians to degrees
arr = np.array([pi/2, pi, 1.5*pi, 2*pi])

x = np.rad2deg(arr)
print(x)

# degrees to radians
arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)
print(x)

# finding angles

x = np.arcsin(1.0)
print(x)
print(np.rad2deg(x))

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
print(np.rad2deg(x))

# hypotenues
x = np.hypot(3, 4)
print(x)