import seaborn as sns 
import matplotlib.pyplot as plt
from numpy import random

x = random.uniform(low=3, high=6, size=(2, 3))
print(x)

sns.kdeplot(random.uniform(low=3, high=6, size=(1000)))
plt.show()