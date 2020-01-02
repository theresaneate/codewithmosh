#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/


import os

# to clear the screen!
os.system("clear")

point = {"x": 1, "y": 2}

# preferred syntax (cleaner)
point = dict(x=1, y=2)

print(point)
print(point["x"])

print("\nReassign x to 11:")
point["x"] = 11
print(point)
print(point["x"])

print("\nAdd z:")
point["z"] = 20
print(point)
print(point["z"])

print("\nCheck for existence of key 'n':")
if "n" in point:
    print("Found N")
else:
    print("N not found")

print("\nUse get method, e.g. .get('a')")
print(point.get("a"))
if point.get("a") is None:
    print("None was returned")
# return 0 if not found - set the default to 0 if no value available
print(point.get("a", 0))

print("\nDelete the kvp of x using del")
del point["x"]
print(point)

# point.items()
print("\n D.items() -> a set-like object providing a view on")
print(point.items())
print("\nIterate through the dictionary using .items()")
for x in point.items():
    print(x)

print("\nSeparate call by key and value")
for key, value in point.items():
    print(key, value)
