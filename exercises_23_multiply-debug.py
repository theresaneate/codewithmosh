#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781741

# F9 for breakpoints
# F5 for debug


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")
