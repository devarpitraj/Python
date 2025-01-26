import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

sns.histplot(x)
plt.show()

sns.histplot(random.poisson(lam=2, size=1000))
plt.show()

sns.kdeplot(random.poisson(lam=2, size=1000))
plt.show()

# normal and poisson ditribution
sns.kdeplot(random.normal(loc=50, scale=7, size=1000), label='normal')
sns.kdeplot(random.poisson(lam=50, size=1000), label='poisson')
plt.legend()
plt.show()

# binomial and poisson distribution
sns.kdeplot(random.binomial(n=1000, p=0.01, size=1000), label='binomial')
sns.kdeplot(random.poisson(lam=10, size=1000), label='poisson')
plt.legend()
plt.show()