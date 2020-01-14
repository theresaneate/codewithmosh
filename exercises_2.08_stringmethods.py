#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781762

import os

# to clear the screen!
os.system("clear")

first = "   Theresa   "
last = "    Neate    "
full = f"{first} {last}"
next = "next char"

print(full, next)
print(full.upper(), next)
print(full.lower(), next)
print(full.title(), next)
# strip only strips leading and following spaces (not middle)
print("\nStripped:")
full = full.strip()
print(full)
print(full, next)
print(full.find("The"))
print(full.replace("Neate", "A surname"))
print("The" in first)
print("The" not in last)
