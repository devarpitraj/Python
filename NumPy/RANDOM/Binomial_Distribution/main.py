from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.binomial(n=10, p=0.5, size=10)
print(x)

sns.displot(x)
plt.show()

sns.kdeplot(x)
plt.show()

sns.kdeplot(random.binomial(n=10, p=0.5, size=1000))
plt.show()

# normal and binomial distribution
sns.kdeplot(random.normal(loc=50, scale=5, size=1000), label='normal')
sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label='binomial')
plt.legend()
plt.show()