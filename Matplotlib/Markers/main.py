import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2, 9, 0, 1, 7, 4])

# marker keyword
plt.plot(ypoints, marker = 's')
plt.show()

# Format Strings fmt
# Syntax = marker|line|color
plt.plot(ypoints, '+-.k')
plt.show()

# markersize or ms
# markeredgecolor or mec
# markerfacecolor or mfc
plt.plot(ypoints, 'o-g', ms = 10, mec = 'r', mfc = 'k')
plt.show()
