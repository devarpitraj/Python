x = 5469839429847196754826587624598436
print(type(x))

x = 34.5
print(type(x))

x = 34e65
print(type(x))

x = 15E6
print(type(x))

x = 14.56e8
print(type(x))

x = 1452.54E6
print(type(x))

x = -3 + 15j
print(type(x))

# int to float
x = float(1)
print(x)

# float to int
x = int(35.56)
print(x)

# int to complex
x = complex(1)
print(x)

# complex to int or float :- not possible
# x = int(1+2j)
# print(x)

# Random Number
import random
print(random.randrange(1, 20))