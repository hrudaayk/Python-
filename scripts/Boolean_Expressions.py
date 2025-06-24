# ...existing code...

# Basic Boolean Expressions

a = 10
b = 20

print(a == b)      # False, checks equality
print(a != b)      # True, checks inequality
print(a > b)       # False, greater than
print(a < b)       # True, less than
print(a >= b)      # False, greater than or equal to
print(a <= b)      # True, less than or equal to

# Logical Operators
print(a < b and b > 15)   # True, both conditions must be True
print(a < b or a > b)     # True, at least one condition is True
print(not (a == b))       # True, negates the result

# Membership Operators
lst = [1, 2, 3]
print(2 in lst)           # True, 2 is in the list
print(5 not in lst)       # True, 5 is not in the list

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)             # True, same object
print(x is z)             # False, different objects with same content
print(x is not z)         # True, not the same object

# ...existing code...

Name = "Hrudaay"
Mobile = 99
Email = "hrudaay007@gmail.com"

#Allows Registraion
#if any field is Filled 
print(any([Name,Mobile,Email]))

#Allows Registraion
#if any field is Filled 
print(all([Name,Mobile,Email]))
#Checks the data type 
print(isinstance(Mobile, int))
#checks the lastletter 
print("Hello".endswith("o"))
#checks the firstletter 
print("Hello".startswith("o"))
