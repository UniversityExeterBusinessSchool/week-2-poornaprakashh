# ======================================
# Python Exercises: Lists, Loops & Tuples
# ======================================
# Save this file as exercises2.py
# Topics covered:
# - Lists and Tuples
# - Organizing and modifying lists
# - Looping through data
# - Using range() and comprehensions
# - Basic statistics
# - Slicing
# - Code styling (PEP 8)
# Learning Objectives:
#   * Store and manipulate collections of data.
#   * Automate repetitive tasks with loops.
#   * Follow basic Python style guidelines.

# ======================================
# 1. Defining and Accessing Lists
# --------------------------------------
# Create a list called fruits with at least three fruit names.
# Print the list.
# Print the first and last items using their index.
fruits = ["apple", "mango", "banana"]
print(fruits)
print(fruits[0])
print(fruits[-1])

# ======================================
# 2. Modifying Lists
# --------------------------------------
# Change the value of the first fruit in your list.
# Add a new fruit to the end of the list using append().
# Insert a fruit at the beginning using insert().
# Remove one fruit using del, one using pop(), and one using remove().
# Print the updated list.
fruits[0] = "blueberry"     #replaces fruit at index 0
print(fruits)
fruits.append("guava")      #inserts guava at the end
print(fruits)
fruits.insert(0, "cherry")  #inserts cherry at index 0
print(fruits)
del fruits[2]               #deletes fruit at index 2
print(fruits)
fruits.pop()                #delets fruit at index -1
print(fruits)
fruits.remove("banana")     #deletes by value
print(fruits)

# ======================================
# 3. Organizing Lists
# --------------------------------------
# Create a list of three or more country names.
# Print the list in alphabetical order using sorted().
# Print the original list to show it is unchanged.
# Sort the list permanently using sort() and print it again.
# Print the list in reverse order using reverse().
# Print the number of countries in the list using len().
countries = ["bulgaria", "morocco", "norway", "australia"]     
print(sorted(countries))   #does not change the order permanently
countries.sort()           #changes the order permanently
print(countries)
countries.reverse()        #changes the order permanently
print(countries)
print(len(countries))

# ======================================
# 4. Avoiding Index Errors
# --------------------------------------
# Try to print an element at an index that doesn’t exist.
# Wrap your code in a try/except block to handle the error gracefully.
                #print(countries[6])

# ======================================
# 5. Looping with for
# --------------------------------------
# Create a list of animals and use a for loop to print each animal’s name.
# Add a message after the loop to thank the user.
zoo = ["baby elephant", "tiger", "cheetah", "koala"]
for animal in zoo:
    print(animal)
print("Thank you")

# ======================================
# 6. Numerical Lists
# --------------------------------------
# Use range() to generate a list of numbers from 1 to 10.
# Print each number using a for loop.
# Create a list of even numbers between 2 and 20 using range().
# Use min(), max(), and sum() to print statistics about your list.
num = list(range(1,11))
for value in num:
    print(value)
num2 = list(range(2,21, 2))
num2
min(num2)
max(num2)
sum(num2)

# ======================================
# 7. List Comprehensions
# --------------------------------------
# Use a list comprehension to create a list of squares (1 to 10).
# Print the list.
numbers = [i*i for i in range(1,11)]
print(numbers)

# ======================================
# 8. Slicing Lists
# --------------------------------------
# Create a list of your favourite foods.
# Print the first three items, middle three items, and last three items using slices.
# Loop through a slice of the list (e.g., first three items) and print each item.
# Make a copy of the list using slicing and modify one of them.
food = ["chow mein", "biriyani", "loaded fries", "chicken tandoori", "misal pav", "puttu"]
print(food[ :3])
print(food[2:5])
print(food[-3: ])
for item in food[0:3]:
    print(item)
food_copy = food[:]
food_copy[0] = "pizza"
print(food_copy)
print(food)

# ======================================
# 9. Tuples
# --------------------------------------
# Create a tuple called dimensions with two values (width, height).
# Print each value using a loop.
# Try changing one of the values (should cause an error) and note what happens.
# Reassign the tuple to a new pair of values and print it again.
dimensions = (20,60)
for value in dimensions:
    print(value)
dimensions = (20,80)
print(dimensions)     #wont show an error as the tuple got replaced
#dimensions[1] = 70
#print(dimensions)     #will show error

# ======================================
# 10. Code Styling (PEP 8)
# --------------------------------------
# Review your code and ensure:
# - Indentation is 4 spaces
# - Lines are under 79 characters
# - Use blank lines to separate logical sections
# This exercise is for self-review.


# ======================================
# Final Challenge
# --------------------------------------
# Create a program that:
#   1. Creates a list of favourite movies.
#   2. Prints them sorted alphabetically.
#   3. Loops through and prints each movie with a custom message.
#   4. Creates a tuple of movie ratings (1–5) and prints the average rating.
#   5. Ensures your program follows PEP 8 guidelines.
movies = ["before sunrise", "wall-e", "titanic", "salam namaste", "interstellar"]
movies.sort()
print(movies)
for movie in movies:
    print(f"This {movie} is amazing!")
movie_ratings = (4.7, 3.2, 3.8, 4.3, 4)
print(sum(movie_ratings) / 5)
