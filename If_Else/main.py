if 5 > 2:   # ':' is necessary
    print("5 > 2")  # indentation is mandatory
    
a = 5
b = 10

if a > b:
    print('a > b')
elif a == b:
    print('a == b')
else:
    print('a < b')
    
if a == b:
    print('a == b')
else:
    print('a != b')
    
# short hand if - only for a single statement
if a != b : print('a != b')

# short hand if..else
print("a != b") if a != b else print('a == b')  # this technique is known as conditional expression or ternary operator

# short hand if..elif..else
print('a > b') if a > b else print('a == b') if a == b else print('a < b')

# and, or, not operator
a, b, c, d = 3, 6, 20, 8

if a > b and c > d:
    print("Both True")

if a > b or c > d:
    print('Atleast one is true')
    
if not a > b:
    print('a is not greater than b')
    
# nested if

x = 15

if x > 10:
    print('x > 10')
    if x > 20:
        print('and x > 20')
    else :
        print('but x < 20')
        
# pass statement

if 5 > 2:
    pass