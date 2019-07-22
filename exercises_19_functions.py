#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781765


def increment(number, by):
    return number * by


print("\nThe output of the regular passed in values with no input is:")
print(increment(4, 2))

# notes: a tuple is like a list but is read-only e.g. list [] tuple ()
# see the annotation in function definition!


def incrementtuple(number: int, by: int = 1) -> tuple:
    return(number, number + by)


print("\nThe output of the annotated tuple calculation is:")
print(incrementtuple(2))
print(type(incrementtuple))


# notes: keyword arguments /kwargs:
# A keyword parameter is a parameter whose value is determined
# by having a value assigned
# to the keyword name.


def printgreeting(name, greeting):
    print(greeting + " " + name + "!\n")
    # return


def kwargs():
    inputname = input("\nPlease provide a name: ")
    inputgreeting = input("How would you like to be greeted? ")
    printgreeting(greeting=inputgreeting, name=inputname)


kwargs()
