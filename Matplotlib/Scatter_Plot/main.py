import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(30))
y = np.random.randint(100, size=(30))

# plt.scatter(x, y)
# plt.show()

# multiple scatter plots
# plt.scatter(y, x, color = 'red')
# plt.show()

x1 = np.array([3, 6, 1])
y1 = np.array([4, 0, 8])

# defining color for each observation - color or c arg
# colors = np.array(['hotpink', 'red', 'yellow'])
# plt.scatter(x1, y1, c = colors)
# plt.show()

# using colormap - cmap arg, here c arg is only used not color arg
colors = np.random.randint(100, size=(30))
# plt.scatter(x, y, c = colors, cmap = "prism")
# plt.colorbar()    # used to show the colorbar in the fig
# plt.show()

# size of dots - s argument
sizes = np.random.randint(100, size=(30))
# plt.scatter(x, y, s = sizes)
# plt.show()

# transparency of dots - alpha arg
# plt.scatter(x, y, s = sizes, alpha = 0.5)
# plt.show()

# combining color, size and alpha
plt.scatter(x, y, c = colors, s = sizes, cmap = 'ocean', alpha = 0.5)
plt.colorbar()
plt.show()