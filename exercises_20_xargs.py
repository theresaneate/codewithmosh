#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781740

# xargs pass arbitrary number of arguments to function

# first exercise
print("first - before tweaking, just a regular function:")


def multiply(a, b):
    return a * b


print(multiply(2, 3))

# second exercise
print("second - pass any number of args, and specify input/output as tuple:")

# asterisk before parameter makes the parameter a tuple


def multiply2(*list):
    print(list)


multiply2(2, 3, 4, 5)

# third exercise
print("third - looping over numbers e.g. multiplying them:")


def multiply3(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply3(1, 2, 3, 4))
