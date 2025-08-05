# Loop control statements are used to change the normal flow of a loop — like skipping, stopping, or doing nothing in a loop.

# Break Statement - The break statement is used to immediately exit the loop, even if the condition is still true.
# Syntax
"""
for/while loop:
    if condition:
        break    """

# Example
for i in range(1, 6):
    if i == 3:     # "==" is an relational / comparision operator.
        break  # Exit the loop when i is 3
    print("i =", i)  # prints i = 1
#                             i = 2