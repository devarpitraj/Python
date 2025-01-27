import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.logistic(loc=1, scale=2, size=1000))
plt.show()

# normal and logistic distribution
sns.kdeplot(random.normal(scale=2, size=1000), label='normal')
sns.kdeplot(random.logistic(size=1000), label='logistic')

plt.legend()
plt.show()