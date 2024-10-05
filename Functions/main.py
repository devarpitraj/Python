def myfunc():
    print('Hi from function')
    
myfunc()

# Arguments, args
def myfunc(name):
    print('Hi ' + name)
    
myfunc("Tobias")

# Arbitrary Args, *args
def myfunc(*kids):
    print('Hi ' + kids[2])
    
myfunc('Emily', 'Tobias', 'Linus')

# Keyword Arguments, kwargs
def myfunc(child3, child2, child1):
    print('Hi ' + child1)
    
myfunc(child1 = 'Emily', child2 = 'Tobias', child3 = 'Linus')\
    
# Arbitrary Keyword Arguments, **kwargs
def myfunc(**kid):
    print('His last name is ' + kid['lname'])
    
myfunc(fname = "Emily", lname = 'Rudeus')

# Default Parameter
def myfunc(country = "India"):
    print('I am from ' + country)
    
myfunc()
myfunc('Norway')

# Passing data types as args
def myfunc(food):
    for x in food:
        print(x)
    
fruits = ['A', 'B', 'C']
myfunc(fruits)

# return statement
def myfunc(x):
    return 5 * x
    
print(myfunc(2))

# pass statement
def myfunc():
    pass
    
myfunc()

# Positional-Only Args
# use ", /" after args

def myfunc(x, /):
    print(x)

myfunc(3)

# def myfunc(x, /):
#     print(x)

# myfunc(x = 3) # Error

# Keyword-Only Args
def myfunc(*, x):
    print(x)

myfunc(x = 3)

# def myfunc(*, x):
#     print(x)

# myfunc(3) # Error

# Combining Positional-Only and Keywod-Only 
# Args before ", /" are Positional-Only and args after "*, " are Keyword-Only
def myfunc(a, b, /, *, c, d):
    print(a + b + c + d)

myfunc(3, 4, d = 5, c = 6)

# Recursion
def rec_func(k):
    if(k > 0):
        res = k + rec_func(k - 1)
        print(res)
    else:
        res = 0
    return res

rec_func(6)