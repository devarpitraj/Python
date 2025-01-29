import pandas as pd

# read csv
df = pd.read_csv('Python\sample.csv')
print(df.to_string())
print(df)

# max_rows
print(pd.options.display.max_rows)
pd.options.display.max_rows = 15
print(df)
print(pd.options.display.max_rows)

# read json
df = pd.read_json('Python\csvjson.json')
print(df.to_string())
print(df)