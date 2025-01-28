import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)

# labels
print(myvar[1])

myvar = pd.Series(a, index = ['x', 'y', 'z'])
print(myvar)
print(myvar['z'])

# key/value objects
calories = {
    'day1': 420,
    'day2': 390,
    'day3': 380
}

myvar = pd.Series(calories)
print(myvar)
print(myvar['day3'])

# Data Frames
data = {
    'calories' : [420, 390, 380],
    'duration' : [50, 40, 30]
}

myvar = pd.DataFrame(data)
print(myvar)