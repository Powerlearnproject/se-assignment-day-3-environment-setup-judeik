#let's store a fovourit number
Favourite_number = 73
print(f"My Favourite Number is: {Favourite_number}")

# A String: A string should be in either signle or double qoute
greeting = "Hello, PLP Academy August Cohort 2024"
print(greeting)

# To comment a line of code, you highlight the code and press down CTRL + / i.e. forward slash

# Boolean: True or False 
is_python_fun = True
is_python_boring = False
print(f"Is Python fun? {is_python_fun}")
print(f"Is Python boring? {is_python_boring}")

# Control Flow <> Argument 
temperature = 30
if temperature > 25:
    print("It's hot outside! Wear Shorts.")
elif temperature > 15:
    print("It's warm! Maybe wear a light Jacket")
else:
    print("Brrrr! It's Code. Bundle Up!")
    
# Module: We have two types of module, in-built and customized. A module is a file that contains files or functions

#In-Built Module 
import math
result = math.sqrt(144)
print(f"The square root of 144 is: {result}")

# Custom Module: A module is python code that contain function
# Calling a customized module
import greetings
print(greetings.greet("Prof. Ojobor"))
print(greetings.greet("Everyone"))
