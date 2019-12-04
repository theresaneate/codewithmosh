#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

import os

# to clear the screen!
os.system("clear")

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
print("\nFirst: ")
print(first)

second = {5, 6, 6}
second.add(5)
print("\nSecond: ")
print(second)
second.pop()
print("Length Second: ", len(second))
# add and remove some stuff
print(second)
second.remove(6)
second.add(4)
second.add(7)
print(second)

print("\nThird: ")

# union of both
print(first | second)

# intersection - what's common in both
print(first & second)

# different between 2 sets
print(first - second)

# symmetric differnence (in one or other, but not both)
print(first ^ second)

if 1 in first:
    print("\n1 is in First set")
