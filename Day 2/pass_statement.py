# Loop control statements are used to change the normal flow of a loop — like skipping, stopping, or doing nothing in a loop.

# Pass Statement - The pass statement is a placeholder — it does nothing.
# Used when a statement is required syntactically, but you don’t want to write any code yet.
# Syntax
"""
for/while loop:
    if condition:
        pass   """

# Example
for i in range(1, 6):
    if i == 3:
        pass  # Do nothing when i is 3
    print("i =", i)


# Output
"""
i = 1
i = 2
i = 3
i = 4
i = 5   """
