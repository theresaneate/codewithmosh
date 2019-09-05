#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

letters = ["a", "b", "c"]
print(letters)
print(letters.index("a"))

if "d" in letters:
    print("Found!")
    print(letters.index("d"))
else:
    print("Not found")

print(letters.count("c"))
