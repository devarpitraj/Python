import pandas as pd

# viewing the data
df = pd.read_csv('Python\data.csv')

print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))

# info()
print(df.info())