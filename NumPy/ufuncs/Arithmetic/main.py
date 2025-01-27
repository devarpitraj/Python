import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

z = np.add(x, y)
print(z)

z = np.subtract(x, y)
print(z)

z = np.multiply(x, y)
print(z)

z = np.divide(x, y)
print(z)

z = np.mod(x, y)
print(z)

z = np.remainder(x, y)
print(z)

z = np.power(y, x)
print(z)

z, f = np.divmod(x, y)
print(z, f)

z = np.absolute(x)
print(z)

# Arithmetic conditionally
# syntax : np.ufunc_name(arr1, arr2, where=condition)
print('\n')
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

condition = x > 2
z = np.add(x, y, where=condition)
print(z)
# the output may come like [10 20 33 44 55] or [1 2 33 44 55] because the where paramter doesn't handle the false case values. Thus, if u want specifically x or y arrays values then create a copy first and pass the new array in 'out' parameter
# To eliminate this unexpected behavior always define the result array and then apply the ufunc
z = np.copy(x)
np.add(x, y, out=z, where=condition)
print(z)

condition = np.array([True, True, False, True, False])
n = np.copy(x)
np.add(x, y, out=n, where=condition)
print(n)

z = np.add(x, y, where=(x>2))
print(z)    # [4591870180066957722 4591870180066957722 33 44 55]
# this is also an unexpeceted behavior thus follow the rule
z = np.copy(x)
np.add(x, y, out=z, where=(x>2))
print(z)