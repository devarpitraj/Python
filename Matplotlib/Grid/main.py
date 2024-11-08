import matplotlib.pyplot as plt
import numpy as np

y = np.array([2, 9, 0, 1, 5])

plt.plot(y)

# adding grid lines
plt.grid()
# plt.show()

# specify which grid line to display
# plt.grid(axis = 'both')     #default
plt.grid(axis = 'x')
# plt.show()

plt.grid(axis = 'y')
# plt.show()

# set line properties
plt.grid(c = 'g', ls = '-.', lw = 0.4)
plt.show()