#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

print("\nnumbers.sort:")
numbers = [4, 1, 41, 4, 99, 22]
print(numbers)
print(numbers.sort())
print(numbers)

print("\nreinitialise and use sorted():")
numbers = [4, 1, 41, 4, 99, 22]
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))


print("\nsort a list of tuples:")
items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)