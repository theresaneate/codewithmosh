#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781761

import os

# to clear the screen!
os.system("clear")

# primitive types [int, str, float, bool] are immutable
# also immutable = tuple
# immutable types can sometimes be mutable in memory only

# can seemingly edit the string but this actually points to new memory location

mystring = "hello world"
print(mystring)
print(id(mystring))

mystring = "\ntesting 123"
print(mystring)
print(id(mystring))

# mutable types = lists, dictionaries, sets

myobject = {1, 2, 3}
print(myobject)
print(id(myobject))
print(type(myobject))

print("\n")
myobject = {4, 5, 6}
print(myobject)
print(id(myobject))
print(type(myobject))

myobject = "\ntesting 123"
print(myobject)
print(id(myobject))
print(type(myobject))
