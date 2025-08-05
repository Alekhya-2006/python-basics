# Lists - A list in Python is a collection of items that is ordered, changeable (mutable), and allows duplicate values.
# You can store numbers, strings, or even other lists inside a list.

# Syntax - list_name = [item1, item2, item3, ...]
# Items are separated by commas
# List is enclosed in square brackets [ ]

# Examples

# creating a list

fruits = ["apple", "banana", "pomegranate", "Cherry"]
print(fruits)   # ['apple', 'banana', 'pomegranate', 'Cherry']


# Accessing Elements(Indexing)
# Python uses zero-based indexing, which means first element is index 0.

print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana


# changing values
# we can change the values inside the list.

fruits[1] = "mango"
print(fruits)   # ['apple', 'mango', 'pomegranate', 'Cherry']


# list length
# we can know how many items are there in a list

print(len(fruits))  # Output: 4


# Adding Items
fruits.append("orange")   # Add one item at the end
fruits.insert(1, "grape") # Add one item at index 1
print(fruits)           # ['apple', 'grape', 'mango', 'pomegranate', 'Cherry', 'orange']


# Removing Items
fruits.remove("apple")  # Removes first occurrence
fruits.pop()            # Removes last item
del fruits[0]           # Removes item at index 0
print(fruits)          # ['mango', 'pomegranate', 'Cherry']