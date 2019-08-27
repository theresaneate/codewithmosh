#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781740

numbers = list(range(20))
print(numbers)
print(numbers[0])
print(numbers[-1])

numbers[4] = 100
print(numbers)

for n in numbers:
    print(n)

newrange = tuple(range(3, 6))
print("\nNaughty tuple. Range from 3 to 6:")
print(type(newrange))
print(newrange)
for n in newrange:
    print(n)

jump2 = list(range(3, 20, 2))
print("\nJump 2:")
for n in jump2:
    print(n)

startat1 = list(range(1, 20))
print("\nStart at 1:")
for n in startat1:
    print(n)

print("\nIndexing 0:3 using the above list: ")
print(startat1[0:3])

print("\nIndexing :3 using the above list: ")
print(startat1[:3])

print("\nIndexing 0: using the above list: ")
print(startat1[0:])

print("\nIndexing : using the above list: ")
print(startat1[:])

print("\nIndexing 1::2 step using the above list: ")
print(startat1[1::2])

print("\nIndexing ::-1 step using the above list: ")
print(startat1[::-1])
