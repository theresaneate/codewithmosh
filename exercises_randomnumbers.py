#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/
import random


# Make a program that creates a random number and stores it into x.
x = random.random()
print(x)

# Make a program that prints 3 random numbers.
print(random.randrange(100))
print(random.randrange(0, 101, 2))

randomlist = [1, 2, 3, 4]

for x in randomlist:
    print(x)

# print(random.getstate())

# Create a program that generates 100 random numbers and find the frequency of each number.
