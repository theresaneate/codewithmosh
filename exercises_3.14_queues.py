#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

from collections import deque

import os

# to clear the screen!
os.system("clear")

# queues are lists but require you to import collections.deque class
# and to convert a list with deque

myqueue = deque(["Theresa", "Ben, Joe"])

print("\nAdding a 1 using append")
myqueue.append(1)
print(myqueue)

print("\nPopleft")
myqueue.popleft()
print(myqueue)

print("\nPop")
myqueue.pop()
print(myqueue)

print("\nCheck if empty with 'if not 'myqueue':")
if not myqueue:
    print("empty")
else:
    print("not empty")
