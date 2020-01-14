#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781747

import os

# to clear the screen!
os.system("clear")

first = "Theresa"
last = "Neate"

print("clunky way:")
full = first + " " + last
print(full)

print("\nformatted way:")
# f can be upper F or lowercase
full = f"{first} {last}"
print(full)

# use string methods
length = f"{len(first)} {last}"
print(length)

# use expressions
expression = f"{first} {2 * 2}"
print(expression)

# The below from additional material:
# https://realpython.com/python-string-formatting/

name = input("\nPlease input your name: ")

# 1 “Old Style” String Formatting (% Operator)
print("1. Hello, %s" % name)

# 2 “New Style” String Formatting (str.format)
print("2. Hello, {}".format(name))

# 3 String Interpolation / f-Strings (Python 3.6+)
# https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
print(f'3. Hello, {name}!')

print("\nMultiple f-strings:")
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)
