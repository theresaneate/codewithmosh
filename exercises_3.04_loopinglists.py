#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

letters = ["a", "b", "c"]

print("*looping through just a list of letters:")
for letter in letters:
    print(letter)

print("\n*looping enumerate of letters, returns a read-only tuple:")
mytuple = enumerate(letters)
print(mytuple)
for letter in mytuple:
    print(letter)

print("\n*ugly syntax, looping enumerate of letters:\n")
for letter in enumerate(letters):
    print(letter)
    print(letter[0], letter[1])

print("\n*list unpacking, looping enumerate(letters):")
# the following line unpacks enumerate letters into index & letter
for index, letter in enumerate(letters):
    print(enumerate(letters))
    print(letters)
    print(index, letter)
