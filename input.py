# input() statement is used to accept values from the user.

# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for their age
age = input("Enter your age: ")   
# age = int(input("Enter yout age: "))    # We can add that age is a integer here only. Then we don't need to convert again



# Convert age to integer

age = int(age) 

# Print a greeting  

# print("Hello,", name,"! You are", age, "years old.")
print(f"Hello, {name}! You are {age} years old.")    # We can use the both ways