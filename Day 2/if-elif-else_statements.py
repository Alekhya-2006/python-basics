# Conditional Statements - Conditional statements are used to make decisions in your code based on conditions.

# If-elif-else Statements - Used when you have multiple conditions to check. Python evaluates them in order and runs the first true condition.
# Syntax
"""
if condition1:
    block 1
elif condition2:
    block 2
elif condition3:
    block 3
else:
    block if none are true    """

# Example

# This program simulates a traffic light system using if-elif-else statements

# Set the current color of the traffic light
light = "white"

# Check if the light is red
if(light == "red"):
    print("Stop")  # If the light is red, vehicles must stop

# Check if the light is green
elif(light == "green"):
    print("Ygo.")  # If the light is green, vehicles can move

# Check if the light is yellow
elif(light == "yellow"):
    print("look")  # If the light is yellow, vehicles should slow down and prepare to stop

# If the light is not red, green, or yellow, handle the unexpected case
else:                                  
    print("light is broken.")  # If the light has an unknown color, assume it's broken
