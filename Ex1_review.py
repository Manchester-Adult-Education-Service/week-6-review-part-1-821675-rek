# -------------------------------------------
# Exercise 1: Revision
# -------------------------------------------
# In this exercise, you’ll review the core Python concepts you’ve learned so far
# (variables, input, if/else, loops, and operators)
# and also explore one *new idea*: **string methods**.
#
# String methods are built-in functions that let you modify or check text easily.
# Example:
#   text = "HELLO"
#   print(text.lower())  # makes the text lowercase → "hello"
#
# You’ll see some new methods in this exercise like:
#   .lower()   → converts text to lowercase
#   .upper()   → converts text to uppercase
#   .strip()   → removes extra spaces before/after a word
#
# Don’t worry — we’ll explain what each one does as you use it.
# -------------------------------------------


# Task 1: User Input & Variables Review
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: User Input & Variables Review\n"
    + "-------------------------------------------")
# In this task, you’ll practise collecting input and using variables.
#
# TODO:
# 1. Ask the user for their name and age.
# 2. Use the .strip() method on their name to remove any extra spaces.
# 3. Convert their age to an integer using int() — because input() gives you a string!
# 4. Print a friendly message with their name and age.
#
# Example:
# Enter your name:   Alice
# Enter your age:  20
# Output: "Hello, Alice! You are 20 years old."
#
# Hint: Remember to use f-strings for clear formatting.
#
# Write your code below:
name=input("Enter your name:\n").strip()
age=int(input("Enter your age?\n"))
print(f"Hello, {name}! You are {age} years old.")


# Task 2: Decision Making (if / else)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Decision Making (if / else)\n"
    + "-------------------------------------------")
# Let’s review conditional logic.
#
# TODO:
# 1. Ask the user for their favourite colour.
# 2. Use the .lower() method to make their answer lowercase (so “Blue” and “blue” both work). 
# 3. Use if/elif/else to:
#    - Print “Nice choice!” if the colour is “blue”.
#    - Print “That’s a bright choice!” if the colour is “yellow”.
#    - Otherwise, print “That’s an interesting colour!”
#
# Example:
# Enter your favourite colour: BLUE
# Output: "Nice choice!"
#
# Write your code below:
colour=input("Enter your favourite colour: ").lower()
if colour=="blue":
    print ("Nice choice!")
elif colour=="yellow":
    print ("That's a bright choice!")
else:
    print("That's an interesting colour!")

# Task 3: Loops Review (for and while)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Loops Review (for and while)\n"
    + "-------------------------------------------")
# Here, you’ll combine loops with input and conditions.
#
# TODO:
# 1. Ask the user for a number between 1 and 10.
# 2. Use int() to convert it into an integer.
# 3. Use a for loop to print the multiplication table for that number (1 to 10).
# 4. After the for loop, ask: “Do you want to try another number? (yes/no)”
# 5. Use a while loop to repeat the program while the user answers “yes”.
# 6. Use .lower() to make the answer comparison work even if they type “YES” or “Yes”.
#
# Hint: The while loop will continue until the user types “no”.
#
# Example:
# Enter a number: 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# (Continue until 3 x 10)
# ...
# Do you want to try another number? yes
# (loops again)
#
# Write your code below:
user="yes"
while user=="yes":
    number=int(input("Please enter a number between 1 and 10: "))
    print("the number you entered is {number}: ")
    for i in range (1,11):
        print(f"{number} x {i} = {number * i}")
    user=input("Do you want to try another number : yes or no: ").lower()

#        
# -------------------------------------------
# Submitting Your Work (after Tasks 1–3)
# -------------------------------------------
# Once you’ve completed the 3 basic tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Username Generator
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Username Generator\n"
    + "-------------------------------------------")
# Create a small program that builds a simple username.
#
# TODO:
# 1. Ask the user for their first name and favourite number.
# 2. Convert the name to lowercase using .lower().
# 3. Combine them into a username and print it.
# Example:
# Enter your first name: Alice
# Enter your favourite number: 7
# Output: "Your username could be: alice7"
#
# Write your code below:
name=input("what is your first name? :").lower().strip()
number=int(input("please enter your favourite number: "))
print(f"{name}{number}")

# Extension 2: Counting with Conditions
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2: Counting with Conditions\n"
    + "-------------------------------------------")
# Let’s practise loops and comparison operators.
#
# TODO:
# 1. Ask the user for a number (int).
# 2. Use a for loop to print all numbers from 1 up to that number.
# 3. If a number is even, print “Even number found!”
# 4. If it’s odd, print “Odd number found!”
#
# Hint: Use the modulus operator % to check even/odd.
# Example: if num % 2 == 0 → even number.
#
# Write your code below:
number=int(input("please enter a number: "))
for i in range (1, number):
    print(f"{i}")
if number % 2 == 0:
    print(f"Even number found!")
else:
    print(f"Odd number found!")

# Extension 3: Simple Password Checker
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3: Simple Password Checker\n"
    + "-------------------------------------------")
# Create a mini login system.
#
# TODO:
# 1. Set a variable called password and assign it a value (e.g. "python123"). We want to store the correct password here.
# 2. Ask the user to enter a password.
# 3. Use .strip() and .lower() to normalise (take out spaces and convert to lowercase) their input.
# 4. Use an if statement to check if it matches your stored password.
# 5. If correct, print “Access granted.”
# 6. Otherwise, print “Access denied.”
# 7. Allow up to 3 attempts using a while loop.
#
# Hint: You’ll need a counter variable to track attempts.
#
# Example:
# Enter password: python123
# Output: Access granted.
#
# Write your code below:
password="python123"
user_password=input("please enter a password: ").lower().strip()
count = 0
while user_password!=password and count < 2:
    print(f"Access denied.")
    user_password=input("please enter a password: ").lower().strip()
    count = count + 1
if user_password==password:
    print(f"Access granted.")

# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# Combine everything you’ve learned into a mini interactive program!
#
# Mini Challenge: “Student Score Checker”
# -------------------------------------------
# 1. Ask the user for a student’s name and three test scores.
# 2. Use int() to convert each score to an integer.
# 3. Calculate the average score.
# 4. Use if/elif/else to give feedback:
#    - 70 or more → "Excellent!"
#    - 50–69 → "Good effort!"
#    - below 50 → "Needs improvement."
# 5. Print a summary showing the student name (using .title()), scores, and average.
#
# Example:
# Enter name:   emma
# Enter score 1: 70
# Enter score 2: 65
# Enter score 3: 80
# Output:
# Student: Emma
# Average: 71.7
# Excellent!
#
# Write your code below:
name=input("please enter your name: ")
scores=[]
for i in range (1,4):
    scores.append(float(input(f"please enter score {i}: ")))
print(f"student name: {name}") 
average=sum(scores)/len(scores)
print(f"average {average}")
if average >=70: 
    print(f"Excellent!")
elif average >=50 and average <70:
    print(f"Good effort!")
else:
    print(f"Needs improvement!")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
