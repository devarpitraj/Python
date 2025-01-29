import pandas as pd

df = pd.read_csv('Python/data.csv')

print(df.corr())