from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# distplot is deprecated use displot or histplot or kdeplot a/c to the needs
# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
sns.kdeplot([0, 1, 2, 3, 4, 5])
plt.show()