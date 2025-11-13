# ==============================
# Beginner Python Exercises
# ==============================
# Save this file as exercises.py

# Exercise 1: Variables
# ---------------------
# Create a variable called name and assign it your first name.
# Print the variable to the screen.
name = "Poorna"
print(name)

# Exercise 2: Numbers
# ---------------------
# Create two variables, x and y, and assign them the values 5 and 10.
# Print their values.
x = 5
y = 10
print(x, y)

# Exercise 3: Arithmetic Operators
# ---------------------------------
# Using x and y from above, calculate and print:
#   - The sum
#   - The difference (x - y)
#   - The product
#   - The quotient
print(f"The sum of x and y is {x+y}")
print(f"The difference of x and y is {x-y}")
print(f"The product of x and y is {x*y}")
print(f"The quotient of x and y is {x/y}")


# Exercise 4: Strings
# ---------------------
# Create a variable greeting with the value "Hello".
# Create another variable person with your name.
# Print them together in one sentence (concatenate strings).
greeting = "Hello"
person = "Poorna"
print(greeting + " " + person)
#this line will print my name

# Exercise 5: Comments
# ---------------------
# Add a comment above a line of code explaining what it does.
# Example: # This line prints my name


# Exercise 6: Logical Operators
# ------------------------------
# Create two boolean variables: is_sunny = True, is_warm = False.
# Use logical operators to print:
#   - is_sunny AND is_warm
#   - is_sunny OR is_warm
#   - NOT is_sunny
is_sunny = True
is_warm = False
print(is_sunny and is_warm)
print(is_sunny or is_warm)
print(not is_sunny)

# Exercise 7: Combining Concepts
# -------------------------------
# Ask the user for their age using input().
# Convert it to an integer.
# Print whether they are old enough to vote (18 or older).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Exercise 8: Challenge
# ---------------------
# Ask the user for two numbers.
# Print:
#   - Their sum
#   - Whether the first number is greater than the second
#   - Whether the numbers are equal
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
elif num1==num2:
    print("Both numbers are equal")

# Extra Challenge 1
# -----------------
# Ask the user for their name and age.
# Print a message: "Hello <name>, you will be <age+1> next year."
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}, you will be {age + 1} next year")

# Extra Challenge 2
# -----------------
# Ask the user for a number.
# Print whether the number is even or odd.
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")

# Extra Challenge 3
# -----------------
# Create two string variables with any words.
# Print the total number of characters in both words combined.
string1 = "dinosaur"
string2 = "meatballs"
print(len(string1) + len(string2))

string3 = "kiki  "
string4 = "mo"
print(len(string3) + len(string4))

# Extra Challenge 4
# -----------------
# Ask the user for their age and whether it is sunny (True/False).
# Print whether they are allowed to go outside if they are at least 12 years old AND it is sunny.
age = int(input("What is your age? "))
sunny = input("Is it sunny today? (True/False) ")
if age >= 12 and sunny == True:
    print("You can go outside and enjoy the sun")
else:
    print("You will have to sit at home")

# Final Project: Mini Program
# ----------------------------
# Create a simple program that:
#   1. Asks the user for their name and greets them.
#   2. Asks for their age and tells them if they can vote.
#   3. Asks for two numbers and shows their sum, difference, product, and quotient.
#   4. Prints a farewell message that includes their name.
name = input("What is your name? ")
print(f"Nice to meet you {name}")
age = int(input("Please enter your age: "))
if age >= 18:
    print("You can vote")
else: 
    print("You will have to wait till you are 18 to vote")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
print(f"The sum is {num1+num2}")
print(f"The difference is {num1-num2}")
print(f"The product is {num1-num2}")
print(f"The quotient is {num1/num2}")

print(f"Thank you so much for your time {name}")