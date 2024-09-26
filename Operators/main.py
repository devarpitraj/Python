# Arithmetic Operators

x = 15
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print('\n')

# Assignment Operators

x = 5
x += 5
x -= 2
x *= 18
x /= 4
x %= 2
x //= 3
x **= 2

y = 5
y &= 3
y |= 4
y ^= 2
y >>= 2
y <<= 1
print(x := 3)
print('\n')

# Comaprison Operators

x = 2

print(x == 5)
print(x != 5)
print(x > 5)
print(x < 5)
print(x >= 5)
print(x <= 5)
print('\n')

# Logical Operators

x = 2

print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not((x < 5 and x < 10)))
print('\n')

# Identity Operators

x = ["apples", "bananas"]
y = ["apples", "bananas"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print('\n')

# Membership Operators

x = ["apples", "bananas"]

print("bananas" in x)
print("pine" not in x)
print('\n')

# Bitwise Operators

x = 5

print(x & 1)
print(x | 1)
print(x ^ 1)
print(~x)
print(x << 2)
print(x >> 1)
print('\n')