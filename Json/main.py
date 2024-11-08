import json

# some json string
x = '{"name" : "John", "age" : 30}'

# convert json to python
y = json.loads(x)

print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert python obj to json
y = json.dumps(x)

print(y)

print(json.dumps(x, indent = 4))
print(json.dumps(x, indent = 4, separators = (".", "=")))
print(json.dumps(x, indent = 4, sort_keys = True))