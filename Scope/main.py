# Local Scope

def func():
    x = 30
    print(x)
    
func()

# function inside function

def f1():
    x = 300
    def f2():
        print(x)
    f2()
    
f1()

# Global Scope

x = 400

def func():
    print(x)
    
func()
print(x)

x = 800

def myfunc():
    x = 200
    print(x)
    
myfunc()
print(x)

# global Keyword

def func():
    global x
    x = 100
    
func()
print(x)

x = 900

def func():
    global x
    x = 1000
    
func()
print(x)

# nonlocal keyword

def myfunc1():
    x = "Hi"
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()    
    return x

print(myfunc1())