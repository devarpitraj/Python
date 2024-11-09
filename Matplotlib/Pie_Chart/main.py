import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 40])

# simple pie
# plt.pie(y)
# plt.show()

# pie with label
mylabels = np.array(['A', 'B', 'C', "D", 'E'])
# plt.pie(y, labels = mylabels)
# plt.show()

# pie with custom start angle
# plt.pie(y, labels = mylabels, startangle = 135)
# plt.show()

# explode parameter
myexplode = np.array([0.2, 0.5, 0, 0, 0.1])
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.show()

# shadow parameter
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show()

# colors
mycolors = np.array(['black', 'm', '#4CAF50', 'r', 'c'])
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors)
# plt.show()

# legend
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(loc = 'upper right', title = "Four Fruits")
plt.show()