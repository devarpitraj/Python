# variable in placeholder
price = 56
txt = f"Price is {price} rs"
print(txt)

# operations in placeholder
txt = f"Price is {465 + 76} rs"
print(txt)

price = 56
tax = 0.3
txt = f"Price is {(1 + tax)*price} rs"
print(txt)

txt = f"It is {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# functions in placeholder
fruit = 'apples'
txt = f"I love {fruit.upper()}"
print(txt)

def myfun(x):
    return x* 40

txt = f"Price is {myfun(price)} rs"
print(txt)

# Modifiers in plcaeholder
txt = f"price is {price:<8} rs" #left align
print(txt)

txt = f"price is {price:>8} rs" #right align
print(txt)

txt = f"price is {price:^8} rs" #center align
print(txt)

txt = f"price is {-87:=8} rs"   #places the plus/minus sign at the leftmost position
print(txt)

txt = f"price is {56:+} rs"  #Use a plus sign to indicate if the result is positive or negative
print(txt)

txt = f"price is {-9:-} rs" #Use a minus sign for negative values only
print(txt)

txt = f"price is {-6756: } rs" #Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
print(txt)

txt = f"Price is {1000000000000:,} rs"  #Use a comma as a thousand separator
print(txt)

txt = f"Price is {1000000000000:_} rs"  #Use a underscore as a thousand separator
print(txt)

txt = f"Price is {100:b} rs"  #binary format
print(txt)

txt = f"Price is {65:c} rs"  #Converts the value into the corresponding Unicode(ASCII) character
print(txt)

txt = f"Price is {0b0110:d} rs"  #decimal format
print(txt)

txt = f"Price is {1000000000000:e} rs"  #scientific format with a lowercase e
print(txt)

txt = f"Price is {1000000000000:E} rs"  #scientific format with a uppercase E
print(txt)

# fixed point number format
txt = f"price is {price:.2f} rs"
print(txt)
txt = f"price is {price:f} rs"
print(txt)

# Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x = float('inf')

txt = f"Price is {x:f} rs"
print(txt)
txt = f"Price is {x:F} rs"
print(txt)

# octal format
txt = f"Octal format of 5364 is {5364:o}"
print(txt)

# hex format
# lowercase
txt = f"Hex format of 63654 is {63654:x}"
print(txt)

# uppercase
txt = f"Hex format of 63654 is {63654:X}"
print(txt)

# percentage format
txt = f"You scored {0.52:%}"
print(txt)

# with specific no. of decimals
txt = f"You scored {0.52:.2%}"
print(txt)
txt = f"You scored {0.52:.1%}"
print(txt)
txt = f"You scored {0.52:.0%}"
print(txt)