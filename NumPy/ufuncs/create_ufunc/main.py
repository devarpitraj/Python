import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
c = np.add(a, b)    # np.add is a built-in ufunc
print(c)

print(type(np.add))

# create ufunc
def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)  # add your func in numpy ufunc library

a = np.array([1, 2])
b = np.array([3, 4])
c = myadd(a, b)
print(c)