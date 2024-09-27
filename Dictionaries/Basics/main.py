thisdict = {
    "name" : "John",
    "age" : 35,
    "country" : "Norway"
}
print(thisdict)

print(thisdict["name"])

thisdict = {
    "name" : "John",
    "age" : 35,
    "country" : "Norway", 
    "country" : "France"
}
print(thisdict["country"])

print(len(thisdict))

print(type(thisdict))

thisdict = dict(name = "John", age = 65, country = "Norway")
print(thisdict)

# Access items

print(thisdict["name"])

x = thisdict.get("name")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

print("model" in thisdict)
print("model" not in thisdict)

# change values

thisdict["age"] = 46
print(thisdict)

thisdict.update({"age" : 88})
print(thisdict)

# Adding Items

thisdict["salary"] = "300K"
print(thisdict)

thisdict.update({"post" : "SDE"})
print(thisdict)

thisdict.pop("post")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["country"]
print(thisdict)

thisdict.clear()
print(thisdict)

del thisdict
# print(thisdict)

thisdict = {
    "name" : "John",
    "age" : 35,
    "country" : "Norway"
}

# Loop through keys
for x in thisdict:
    print(x)
# OR, 
for x in thisdict.keys():
    print(x)
    
# Loop through values
for x in thisdict:
    print(thisdict[x])
# OR, 
for x in thisdict.values():
    print(x)
    
# Loop through both key and value
for x, y in thisdict.items():
    print(x, y)