#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

# print("\nnumbers.sorted:")
# numbers = [4, 1, 41, 4, 99, 22]
# print(numbers)
# numbers.sort()
# print(numbers)

# print("\nreinitialise and use sorted():")
# numbers = [4, 1, 41, 4, 99, 22]
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))


items = [
    ("Product", 10)
    ("Product", 9)
    ("Product", 12)
]

def sort_item(item):
    item[1]

items.sort(key=sort_item)
print(items)