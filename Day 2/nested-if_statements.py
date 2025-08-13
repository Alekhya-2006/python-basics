# Conditional Statements - Conditional statements are used to make decisions in your code based on conditions.

# Nested If Statements - A nested if is an if statement inside another if or else block.
# Syntax
"""
if condition1:
    if condition2:
        code if both conditions are true    """

# Example
# Sample values for x and y
x = 5
y = 3

# First condition: Check if x is a positive number
if x > 0:
    # Second condition (nested): Check if y is greater than 5
    if y > 5:
        # This block runs only if both conditions are true
        print("x is positive and y is greater than 5")
    else:
        # This block runs if x is positive but y is not greater than 5
        print("x is positive but y is not greater than 5")
else:
    # This block runs if x is not positive (i.e., zero or negative)
    print("x is not positive")
