#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
