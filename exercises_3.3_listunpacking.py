#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other, last = numbers
print("Values:")
print(first)
print(second)
print(other)
print(numbers)
print("Last = " + str(last))
print("\nTypes: ")
print(type(first))
print(type(other))
print(type(numbers))

print("\nUsing a function:")


def multiply(*numbers):
    print(numbers)
    print(type(numbers))


multiply(1, 2, 3)
