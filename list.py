# Basic example of lists in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements by index
print(fruits[0])  # Output: apple
print (fruits[1])  # Output: banana
print (fruits[2])  # Output: cherry

# Modifying an element
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Adding an element
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']

# Removing an element
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Getting the length of the list
print(len(fruits))  # Output: 3