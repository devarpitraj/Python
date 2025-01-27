import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.chisquare(df=2, size=(2, 3))
print(x)

sns.kdeplot(random.chisquare(df=1, size=1000))
plt.show()