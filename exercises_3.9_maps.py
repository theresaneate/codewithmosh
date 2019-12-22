#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

print("The inelegant way first:")
prices = []
for item in items:
    prices.append(item[1])


print(prices)


print("\nThe more elegant map way:")

x = map(lambda item: item[1], items)
for item in x:
    print(item)

print("\nThe list way:")
prices = list(map(lambda item: item[1], items))
print(prices)
