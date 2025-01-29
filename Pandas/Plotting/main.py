import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Python/data.csv')

df.plot()
plt.show()

# scatter plot
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

df.plot(kind='scatter', x="Duration", y='Maxpulse')
plt.show()

# histogram
df['Duration'].plot(kind='hist')
plt.show()