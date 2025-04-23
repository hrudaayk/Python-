#===================================================================
# PRINT()
# ---------------------------------------
# ......
# ......
#===================================================================

print("Hi Python")
print('Hello Python')
# print("Hi')

print("--------------------")
print("    LEARN PYTHON    ")
print("--------------------")

print("           __")
print("          / _)")
print("   .-^^^-/ /  ")
print("__/       /   ")
print("<__.|_|-|_|   ")

# Escape Sequences
# \"
# \'
# print("Hi "Python"")
print("Hi \"Python\"")
print('Hi 'Python'')
print('Hi "Python"')
print('Hi 'Python'')
print('Hi \'Python\'')

# \\
print("Path: C:\Users\Baraa")
print("Path: C:\\Users\\Baraa")

# \n New Line
print("Message1")
print()
print("Message2")

print("Message1\n")
print("Message2")

print("Message1\n\n\nMessage2")

print("Message1\nMessage2")

# \t New Line
print("Message1\tMessage2")

print("Your learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

print("""Your learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI""")

# Why we need really PRINT()
price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 2
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)
discount = subtotal * 0.10
print("Discount:", discount)
final_total = subtotal - discount
print("Final Total:", final_total)
