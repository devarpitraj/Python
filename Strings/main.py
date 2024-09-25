print('hello')
print("hello")

# Quotes inside quotes
print("It's alright")
print("He is 'John'")
print('He is "John"')

# Multiline strings
print("\n")
a = """hello
hi
there
good"""
print(a)

a = '''hello
hi
there
good'''
print(a)

print("\n")

# Strings as arrays
a = "Hello"
print(a[4])

# Looping
for x in "hi":
    print(x)
    
# Length
a = "Hello"
print(len(a))

# Check string
txt = "Hello World"
if "el" in txt:
    print("Yes")
    
if "hi" not in txt:
    print("Yes")
    
b = "Hello, World!"
# slicing a particular section
print(b[2:5])

# slicing from start
print(b[:5])

# slicing to end
print(b[2:])

# Negative Indexing
b = "Hello, World!"

print(b[-5]) # counting starts from 1 from end i.e. ! is -1, d is -2, and so on.
print(b[-5:-2])

print("\n")

# upper()
a = "  Hello, World!  "
print(a.upper())

# lower()
print(a.lower())

# strip() - remove whitespaces
print(a.strip())

# replace()
print(a.replace("l", "i"))

# split()
print(a.split(","))
print(a.split("l"))

# Format strings
age = 36
txt = f"My age is {age} years"  #{} is a placeholder
print(txt)

# Placeholder can contain variables, operations, functions, and modifiers
# Modifier is included by adding a colon(:) followed by a legal formatting type

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

txt = f"The price is {54 * 65} dollars"
print(txt)

a = "Hello, World!"
print(a.casefold()) #converts to lowercase

# All string methods returns new values, they do not change the original string