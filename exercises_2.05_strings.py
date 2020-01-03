#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781742

import os

# to clear the screen!
os.system("clear")

course = "Python Programming"
print(len(course))
print(id(course))
print(course[0])

# negative index, not seen in other program
print(course[-1])


print(course[-2])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))
print(id(course[:]))
