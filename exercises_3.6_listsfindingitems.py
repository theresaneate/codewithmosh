#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

letters = ["a", "b", "c"]
print(letters)
print(letters.index("a"))

if "a" in letters:
    print("Found!")
    # print(letters.index("a"))
else:
    print("Not found")

letters = ["a", "b", "c", "c"]
print(letters.count("c"))
