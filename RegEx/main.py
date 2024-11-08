import re

txt = "The rain in Spain"
x = re.search("The.*Spain$", txt)

print("Match") if x else print("No Match")

# Metacharacters

# [] - a set of chars
x = re.findall('[a-m]', txt)
print(x)

# \ - signals a special sequence
x = re.findall('\s', txt)
print(x)

# . - any char
x = re.findall('T.e', txt)
print(x)

# ^ - starts with
x = re.findall('^The', txt)
y = re.findall('^Te', txt)
print(x, y)

# $ - ends with
x = re.findall('Spain$', txt)
y = re.findall('Span$', txt)
print(x, y)

# * - zero or more occurences
x = re.findall("Th.*n", txt)
y = re.findall('Th.*e', txt)
print(x, y)

# + - one or more occurences
x = re.findall("Th.+e", txt)
y = re.findall('Sp.+i', txt)
print(x, y)

# ? - zero or one occurence
x = re.findall('T.?e', txt)
y = re.findall('T.?n', txt)
z = re.findall("Sp.?n", txt)
print(x, y, z)

# {} - exactly the specified no. of occurences
x = re.findall('T.{6}n', txt)
y = re.findall('T.{9}n', txt)
z = re.findall('T.{15}n', txt)
print(x, y, z)

# | - either or
x = re.findall("rain|freeze", txt)
print(x)


# Special Sequences

# \A - returns a match if the specified chars are at the beginning of the string
x = re.findall('\AThe', txt)
y = re.findall('\Ain', txt)
print(x, y)

# \b - returns a match where the specified chars are at the beginning or end of a word
x = re.findall(r'\bain', txt)
y = re.findall(r'ain\b', txt)
print(x, y)

# \B - returns a match where the specified chars are present BUT NOT at the beginning or at the end of a word
x = re.findall(r'\Bain', txt)
y = re.findall(r'ain\B', txt)
print(x, y)

# \d - returns a match where the string contains a digit
str = 'Hello World 64 the 76'
x = re.findall('\d', str)
print(x)

# \D - returs a match where the string doesn't contain a digit
x = re.findall('\D', str)
print(x)

# \s - returns a match where the string contains white space char
x = re.findall('\s', txt)
print(x)

# \S - returns a match where the string doesn't contain white space char
x = re.findall('\S', txt)
print(x)

# \w - returns a match where the string contains any word chars(chars from a-Z, digits, and underscore(_) char)
txt2 = "Hello _6 *%^ World 5467 hi"
x = re.findall('\w', txt2)
print(x)

# \W - returns a match where the string doesn't contain any word chars
x = re.findall('\W', txt2)
print(x)

# \Z - returns a match if the specified chars are at the end of a word
x = re.findall('Spain\Z', txt)
y = re.findall('in\Z', txt)
z = re.findall('rain\Z', txt)
a = re.findall('The\Z', txt)
print(x, y, z, a)


# Sets

x = re.findall('[arn]', txt)    # returns a match where one of the specified char is present
y = re.findall('[a-n]', txt)    # returns a match for any lowercase char between a and n
z = re.findall('[^arn]', txt)   # returns a match for any char except a, r, and n
print(x)
print(y)
print(z)

x = re.findall('[0123]', str)
y = re.findall('[0-9]', str)
z = re.findall('[0-6][3-6]', str)
print(x)
print(y)
print(z)

x = re.findall('[a-zA-Z]', txt)
print(x)

x = re.search(r'\bS.*', txt)
print(x.group())