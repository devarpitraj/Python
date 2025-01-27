import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random

x = random.pareto(a=2, size=(2, 3))
print(x)

sns.histplot(random.pareto(a=2, size=1000))
plt.show()