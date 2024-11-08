import matplotlib.pyplot as plt
import numpy as np

# line drawing
xpoints = np.array([1, 9])
ypoints = np.array([0, 7])

plt.plot(xpoints, ypoints)
plt.show()

# only points
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple points
xpoints = np.array([1, 6, 2, 9, 13])
ypoints = np.array([3, 9, 0, 4, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default X-points
ypoints = np.array([6, 1, 9, 0, 3, 1])

plt.plot(ypoints)
plt.show()