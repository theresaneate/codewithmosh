#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

print("\nFrom previous exercise:")


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


print("\nLambda:")


items.sort(key=lambda item: item[1])
print(items)
