"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

a = "Hello"
print(a, type(a))

b = 20
print(b, type(b))

c = 20.5
print(c, type(c))

d = 1j
print(d, type(d))

e = ["apple", "banana"]
print(e, type(e))

f = ("apple", "banana")
print(f, type(f))

g = range(7)
print(g, type(g))

h = {"name" : "John", "age" : 53}
print(h, type(h))

i = frozenset({"apple", "banana", "cherry"})
print(i, type(i))

j = True
print(j, type(j))

k = b"Hello"
print(k, type(k))

l = bytearray(8)
print(l, type(l))

m = memoryview(bytes(6))
print(m, type(m))

n = None
print(n, type(n))