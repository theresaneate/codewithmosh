#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

x = 10
y = 11


def printing():
    print("\nprint X and Y")
    print(x, y)


printing()

print("\nUnpacking a tuple : x, y = y, x / similar to x, y = (y, x)")
x, y = y, x
printing()
