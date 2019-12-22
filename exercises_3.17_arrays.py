#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/


from array import array
import os

# to clear the screen!
os.system("clear")


# arrays need a typecode as first parameter,
# in our case it's i for 'signed integer' (i.e. both neg/pos int)

numbers = array("i", [1, 2, 3])


def outputArray():
    for item in numbers:
        print(item)
    print(numbers)


numbers.append(55)
print("\nnumbers.append(55)")
outputArray()

numbers.remove(2)
print("\nremove(2)")
outputArray()

numbers.pop()
print("\npop()")
outputArray()

print("\nnumbers[0]")
print(numbers[0])
outputArray()
