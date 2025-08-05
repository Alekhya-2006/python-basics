# Loop control statements are used to change the normal flow of a loop — like skipping, stopping, or doing nothing in a loop.

# Continue Statements - The continue statement skips the current iteration and moves to the next one in the loop.
# Syntax
"""
for/while loop:
    if condition:
        continue    """

# Example
for i in range(1, 6):
    if i == 3:
        continue  # Skip printing when i is 3
    print("i =", i)

# Output    
"""
i = 1
i = 2
i = 4
i = 5    """