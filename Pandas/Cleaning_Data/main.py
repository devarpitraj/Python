import pandas as pd

# Null Values-------------

df = pd.read_csv('Python\data.csv')
print(df.info())

# remove rows
new_df = df.dropna()
print(new_df.info())

# inplace=True
df.dropna(inplace=True)
print(df.info())

df = pd.read_csv('Python\data.csv')

# replace empty values
new_df = df.fillna(130)
print(new_df.info())

# replace only for specified columns
new_df = df['Calories'].fillna(130) # new_df will contain the 'Calories' column
print(new_df.info())
# To make the change in original use inplcae=True
# df['Calories'].fillna(130, inplace=True)

# replace using mean(), median(), mode()
x = df['Calories'].mean()
# x = df['Calories'].median()
# x = df['Calories'].mode()

df['Calories'].fillna(x, inplace=True)
print(df.info())

# Wrong Format--------

# change the format of cells into the same format
# df['Date'] = df.to_datetime(df['Date'])

# Wrong Data---------

# replace the data
# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.loc[x, 'Duration'] = 120

# remove the row
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.drop(x, inplace=True)

# Removing Duplicates-----------------

# discover duplicates
print(df.duplicated())

# remove duplicates
df.drop_duplicates(inplace=True)