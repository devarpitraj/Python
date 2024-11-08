import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 6, 2, 8, 3, 10])

# linestyle or ls
plt.plot(ypoints, ls = '--')
plt.show()

# color or c
plt.plot(ypoints, c = 'm')
plt.show()

plt.plot(ypoints, c = '#4CAF50')
plt.show()

plt.plot(ypoints, c = 'red')
plt.show()

# linewidth or lw
plt.plot(ypoints, lw = '20.5')
plt.show()

# Multiple Lines
y2 = np.array([3, 5, 7, 1, 3, 2])

plt.plot(ypoints)
plt.plot(y2)
plt.show()

x1 = np.array([1, 4, 6, 2])
y1 = np.array([3, 0, 2, 6])
x2 = np.array([2, 9, 0, 1])
y2 = np.array([5, 7, 6, 1])

plt.plot(x1, y1, x2, y2)
plt.show()