import seaborn as sns 
import matplotlib.pyplot as plt
from numpy import random

x = random.zipf(a=2, size=(2, 3))
print(x)

x = random.zipf(a=2, size=1000)
sns.histplot(x[x<10])
plt.show()