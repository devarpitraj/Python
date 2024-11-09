import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D', 'E'])
# x = np.array([1, 2, 3, 4, 5])
y = np.random.randint(100, size=(5))

# vertical bars
plt.bar(x, y, color = 'yellow', width = 0.2)
plt.show()

# horizontal bars
plt.barh(x, y, color = 'hotpink', height = 0.4)
plt.show()