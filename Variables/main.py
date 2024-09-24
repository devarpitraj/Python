"""
This is another way of commenting in python
"""

x = 5   # x is type of int
y = "Arpit" # x is now of type str
print(x, y)

# Type casting
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)
print(type(x))
print(type(x), type(y), type(z))

# string variables
x = "John"
X = 'John'
print(x, X)

# Many Values to Multiple Variables
x, y, z = "Orange", 5, 15.46
print(x, y, z)

# One Value to Multiple Variables
x = y = z = 61
print(x, y, z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "There"
y = "is"
z = "difference"
print(x, y, z)
print(x + y + z)    #there is no spaces applied between strs

x = 5
y = 10
print(x + y)

z = "John"
#print(x + z)    #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(x, z)

# Global Variables
x = "Global"

def myfunc():
    x = "Local"
    print("Here x is " + x + " variable")

myfunc()
print("Here x is " + x + " variable")

# global keyword - make global variable inside a func
def myfunc():
    global x
    x = "global inside func"

myfunc()
print(x)

# also u can change global variable value inside a func
x = "hi"

def myfunc():
    global x
    x = "hello"
    
myfunc()
print(x)