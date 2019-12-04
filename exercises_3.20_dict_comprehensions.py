#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/


from array import array
import os

# to clear the screen!
os.system("clear")

values = []
for x in range(5):
    values.append(x * 2)
    print(values)

print("\nUsing List Comprehension:")
values = [x * 2 for x in range(5)]
print(values)

print("\nUsing Set Comprehension:")
values = {x * 2 for x in range(5)}
print(values)

print("\nUsing Dictionary Comprehension:")
values = {x: x * 2 for x in range(5)}
print(values)
