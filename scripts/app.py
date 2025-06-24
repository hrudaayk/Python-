#Advanced Cleaning 
#Clean the string and Output should be - name: maria | role: data engineer | age: 27y
import random
Name = "968-Maria (D@t@ Engineer);; 27y "

print(Name.lower().replace("968-","name: ").replace("@","a").replace(");;"," | age:").strip("y").replace("(","| role: "))

X = (random.randint(1,100))
if X % 2 == 0:
    print(f"{X} is an Even number")
else:
    print(f"{X} is an odd number")

Name = "Hrudaay"
Mobile = 99
Email = "hrudaay007@gmail.com"

print(any([Name,Mobile,Email]))
print(all([Name,Mobile,Email]))

print(isinstance(Mobile, int))

print("Hello".endswith("o"))

print("Hello".startswith("H"))



