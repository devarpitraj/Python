import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 10, 350)

plt.hist(x, color = 'red')
plt.show()