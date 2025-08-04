# Conditional Statements - Conditional statements are used to make decisions in your code based on conditions.

# If-else Statements - The if-else statement allows you to run one block if the condition is true, and another block if it's false.
# Syntax
"""
 if condition:
     code if condition is true  
 else:
     code if condition is false     """
     
# Example
age = 15
if age >= 18:                     
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  # since the condition is not true, it prints "You are not eligible to vote."



# Ternary Operatior( One Line if-else) - Also called conditional expressions, these allow if-else in one line.
# syntax - output_if_true if condition else output_if_false  

# Example
food = "cake"
print("This food item contains sweet.") if food == "cake" or food == "biryani" else print("This food item does not contain sweet.")