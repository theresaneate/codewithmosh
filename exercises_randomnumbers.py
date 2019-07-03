<<<<<<< HEAD
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
=======
# https://pythonbasics.org/exercises/
# Random numbers
import random

# just a method to convert & print X


def printx(x):
    x = str(x)
    print("X is " + x)


# Make a program that creates a random number and stores it into x.
x = random.random()
printx(x)

# Make a program that prints 3 random numbers.
iterator = 1

print("\nbegin loop")

while iterator < 4:
    x = random.randint(0, 10)
    printx(x)
    iterator += 1

print("end of loop\n")

>>>>>>> 791ad9fda257c6de2b8f1fcc826cb2df47e725a7

# Create a program that generates 100 random numbers and find the frequency of each number.
