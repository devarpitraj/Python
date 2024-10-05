x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

# use lambda function when an anonymous function is required for a short period of time
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(2))
print(mytripler(5))