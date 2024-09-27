myfamily = {
    "child1" : {
        "name" : "Emily",
        "age" : 35
    },
    "child2" : {
        "name" : "John",
        "age" : 23
    },
    "child3" : {
        "name" : "Tobias",
        "age" : 34
    }
}
print(myfamily)

# Or,
child1 = {
    "name" : "Emily",
    "age" : 32
}

child2 = {
    "name" : "John",
    "age" : 42
}

child3 = {
    "name" : "Tobias",
    "age" : 52
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

# Access
print(myfamily["child2"]["age"])

# Loop
for x, obj in myfamily.items():
    print(x + ':- ')
    for y in obj:
        print(y + ': ' + str(obj[y]))