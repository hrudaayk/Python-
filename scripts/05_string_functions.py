# ...existing code...

# Basic String Functions in Python

s = "  Hello, World!  "

print(s.lower())           # hello, world!
print(s.upper())           # HELLO, WORLD!
print(s.title())           # Hello, World!
print(s.capitalize())      #   hello, world!
print(s.strip())           # Hello, World! (removes leading/trailing spaces)
print(s.lstrip())          # 'Hello, World!  ' (removes leading spaces)
print(s.rstrip())          # '  Hello, World!' (removes trailing spaces)
print(s.replace("World", "Python"))  # '  Hello, Python!  '
print(s.find("World"))     # 9 (index of substring)
print(s.count("l"))        # 3 (number of occurrences)
print(s.startswith("  He")) # True
print(s.endswith("!  "))   # True
print(s.split(","))        # ['  Hello', ' World!  ']
print(s.join(["A", "B"]))  # 'A  Hello, World!  B'
print(s.isalpha())         # False (contains spaces and punctuation)
print(s.isdigit())         # False
print(s.isalnum())         # False
print(s.isspace())         # False
print(s.swapcase())        # '  hELLO, wORLD!  '
print(s.center(20, "*"))   # '**  Hello, World!  ***'
print(s.zfill(20))         # '0000  Hello, World!  '

# ...existing code...

#Advanced Cleaning 
#Clean the string and Output should be - name: maria | role: data engineer | age: 27y

Name = "968-Maria (D@t@ Engineer);; 27y "
print(Name.lower().replace("968-","name: ").replace("@","a").replace(");;"," | age:").strip("y").replace("(","| role: "))
