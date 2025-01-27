import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random
import numpy as np

x = random.rayleigh(scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.rayleigh(size=1000))
plt.show()