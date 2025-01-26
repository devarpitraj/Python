import numpy as np

# hard coded filter array
arr = np.array([1, 2, 3])
filter_arr = [True, False, True]
newarr = arr[filter_arr]
print(newarr)

# create filter array based on conditions
arr = np.array([41, 42, 43, 44])

filter_arr = []

for ele in arr:
    if ele > 42: filter_arr.append(True)
    else: filter_arr.append(False)
    
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# better way
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)