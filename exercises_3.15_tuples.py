#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/


import os

# to clear the screen!
os.system("clear")


point = (1, 2)


def checkPoint():
    print("Value of point is: " + str(point))
    print("Type is: " + (str(type(point))))


print("\nadding in (1,2)")
checkPoint()

point = 3,
print("\nadding in 3,")
checkPoint()

point = 1
print("\nadding in 1")
checkPoint()

point = ()
print("\nadding in () ")
checkPoint()

point = (1, 2) + (3, 4)
print("\nadding in (1,2) + (3,4) ")
checkPoint()

point = (1, 2) * 3
print("\nadding in (1, 2) * 3 ")
checkPoint()

point = tuple([1, 2])
print("\nadding in tuple([1, 2]) - converting a list to tuple ")
checkPoint()

point = tuple("Hello World")
print("\nadding in tuple('Hello World') - converting a string to tuple ")
checkPoint()

point = (1, 2, 3)
print("\nPrinting point[0:2]")
print(point[0:2])

x, y, z = point
print("\nx, y, z = point")
checkPoint()
print("Value of X is : " + str(x))
