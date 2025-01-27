import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random

x = random.exponential(scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.exponential(size=1000))
plt.show()