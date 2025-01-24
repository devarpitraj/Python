import numpy as np

arr = np.array([1, 2, 3])

x = arr.copy()
y = arr.view()

arr[0] = 42

print(arr)
print(x)
print(y)

y[1] = 43

print(arr)
print(x)
print(y)

# check if array owns its data
# copy array returns None
# view array returns the original object

print(x.base)
print(y.base)