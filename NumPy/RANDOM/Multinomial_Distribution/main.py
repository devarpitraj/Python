import seaborn as sns 
import matplotlib.pyplot as plt
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

sns.kdeplot(x)
plt.show()