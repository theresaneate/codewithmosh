#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781742

import os

# to clear the screen!
os.system("clear")

course = "Python Programming"

print("\nLength of string using len()")
print(len(course))

print("\nMemory location of string using id()")
print(id(course))

print("\nFirst character [0]")
print(course[0])

print("\nnegative index, not seen in other program -1, then -2")
print(course[-1])
print(course[-2])

print("\nslice a string [0:3]")
print(course[0:3])

print("\neverything up to index 3")
print(course[:3])

print("\nstart at 0 and don't provide end")
print(course[0:])

print("\nprint whole string")
print(course[:])

print("\nmemory is allocated individually to string and chars (immutable)")
print(id(course))
print(id(course[0]))
print(id(course[:]))
