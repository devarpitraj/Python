# Packing a tuple
tup1 = ("A", 'b', 'c', 'd', 'E')

# Unpacking tuple
(x, y, z, i, e) = tup1
print(x)
print(y)
print(z)
print(i)

(x, y, *z) = tup1
print(x, y, z)

(x, *y, z, i) = tup1
print(x, y, z, i)