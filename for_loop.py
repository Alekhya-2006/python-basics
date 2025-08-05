# Loops - A loop is used to repeat a block of code multiple times. Instead of writing the same code again and again, we use loops to do it automatically.

# For Loop - A for loop is used to iterate over a sequence (like list, string, range).
# Syntax:
"""
for item in sequence:
    Do something with the item   """

# Examples
# Loop through a list
fruits = ["apple", "banana", "cherry"]

# Loop through each item in the list
for fruit in fruits:
    print(fruit)  # Print each fruit one after another.


# Loop using range()
# Range() - range() is a built-in Python function that generates a sequence of numbers.
# It’s commonly used to repeat an action a specific number of times.    

for i in range(5):
    print(i)      # it prints the numbers from 0 to 4 one by one.
