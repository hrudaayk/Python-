# Basic and Advanced Comparison Operators in Python

a = 5
b = 10
c = 15

# Basic Comparison Operators
print(a == b)    # False, equal to
print(a != b)    # True, not equal to
print(a > b)     # False, greater than
print(a < b)     # True, less than
print(a >= b)    # False, greater than or equal to
print(a <= b)    # True, less than or equal to

# Advanced: Chained Comparison Operators
print(a < b < c)         # True, b is between a and c
print(a <= b <= c)       # True, b is between a and c (inclusive)
print(a < b > 7)         # True, b is greater than both a and 7
print(1 == a < 10)       # False, a is not equal to 1 but is less than 10
print(a < b != c > 10)   # True, b > a, b != c, c > 10

# Equivalent to:
print((a < b) and (b < c))      # True

# Chained comparisons with variables and values
x = 8
print(5 < x <= 10)       # True, x is between 5 and 10 (inclusive)
print(1 < x != 7 < 12)   # True, x > 1, x != 7, 7 < 12

# Mixing types (works if types are compatible)
print('a' < 'b' < 'z')   # True, compares ASCII values

# Edge case: all comparisons must be True for the whole chain to be True
print(a < b > c)         # False, b > c is False

# Membership and identity are not part of chained comparisons, but are often used:
lst = [1, 2, 3]
print(2 in lst)          # True
print(a is b)            # False

print(a is not b)        # True, a and b are not the same object

