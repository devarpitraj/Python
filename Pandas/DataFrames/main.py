import pandas as pd

data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

# locate row
print(df.loc[1])

print(df.loc[[1, 2]])

# named indexes
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)

print(df.loc['day3'])
print(df.loc[['day1', 'day2']])

# load files into DataFrame
df = pd.read_csv('Python\sample.csv')
print(df.to_string())
print(df)

# max_rows
print(pd.options.display.max_rows)
pd.options.display.max_rows = 15
print(df)
print(pd.options.display.max_rows)