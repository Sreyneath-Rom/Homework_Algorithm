# # EXERCISE 1
# # Q1: Convert this tree to Python.
x = 0
y = 0
z = 0
if x == 5:
    if y < 6:
        if z <= 11:
             print("nothing")
        else:
             print(2)
    else:
        print(1)
else:
    if y > 3:
       print(3)
    else:
        print("nothing")
# Q2: Converts this tree to Python.
x = 0
y = 0  
if x > 4:
    if y > 3:
        print ("nothing")
    else:
         print (3)
else:
    if y < 2:
         print("nothing")
    else:
         print (1)

# # EXERCISE 2
nbRepeat = 5
for i in range(nbRepeat):
    print("Hello World")

# # EXERCISE 3
number = int(input())
while number > 5:
    print(number)
    number = number - 2

# # EXERCISE 4
user_name =input("name:")
age =int(input("age:"))
print("My name is "+user_name+ ",I am "+str(age)+"years old.")

# EXERCISE 5
user_input = int(input("Enter your number:"))
if user_input < 0:
    user_input = "Negative Number!"
else:
    user_input = "Positive Number"
print(user_input)

# EXERCISE 6
number = int(input("number:"))
if number < 25 :
    print("Dog")
elif number <= 30 :
    print("Cat")
else :
    print("Cow")
# Q1: What must be the range of number to see &quot;Cat&quot;?(30)
# Q2: What must be the range of number to see &quot;Cow&quot;?(31)

# EXERCISE 7
value =""
if value >= 5:
    print("Apple")
elif value <= 10:
    print("Banana")

# Q1: What will be print if value equal to 10?("Banana")

# EXERCISE 8
value =""
if value >10:
    print("Red")
if value <= 10:
    print("Blue")
# Q1: What will be print if value equal to 10?("Blue")

# EXERCISE 9
text = input()
result = ""
for i in range(len(text)):
    result += "x"
    print(result)

# EXERCISE 10
word = input("Enter a string word: ")
number = int(input("Enter a number: "))
if word == "good" and 7 <= number <= 15:
    print("It's good")
elif word == "bad" and (number < 7 or number > 15):
    print("It's bad")
