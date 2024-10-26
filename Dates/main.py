import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

# creating date objects

x = datetime.datetime(2024, 4, 18)
print(x)

print(x.strftime('%a'))