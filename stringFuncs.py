# Strings are 0-based, meaning the first letter of the string is at index position 0, and the last is at the size of the string -1.

greeting = "Hello"

# Get the length. Note this is not 0 based.
print(len(greeting))

# Print spacific indexes.
print(greeting[1])
print(greeting[3])

# Find the given instance in the string.
print(greeting.find("lo"))
