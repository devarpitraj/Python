import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# generate random normal distribution of size 2*3
x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.normal(size=(1000)))
plt.show()