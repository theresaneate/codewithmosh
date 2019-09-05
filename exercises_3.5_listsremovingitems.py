#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

letters = ["a", "b", "c"]
print(letters)

# Add
print("\nAdd")
letters.append("d")
print(letters)
letters.insert(0, "-")
print(letters)

# Remove
print("\nRemove")
letters.pop()
print(letters)

# Remove by index
print("\nRemove by Index")
letters.pop(1)
print(letters)

letters.remove("b")
print(letters)

# delete a range
print("\nDelete a range")
letters = ["a", "b", "c", "d"]
del letters[0]
print(letters)
del letters[0:2]
print(letters)

# clear
print("\nClear all")
letters.clear()
print(letters)
