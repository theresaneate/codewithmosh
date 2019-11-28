#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/

import os

# to clear the screen!
os.system("clear")

# stacks are just lists
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print("\nafter adding 3 appended")
print(browsing_session)

print("\nthe last item by assigning it through pop method, & remainder")
last = browsing_session.pop()
print(last)
print(browsing_session)

print("\nindex counts backwards, of list [1,2,3] index [-1] is 3")
browsing_session.append(3)
print("stack = " + str(browsing_session))
print("-2 = ", + browsing_session[-2])
print("-1 = ", + browsing_session[-1])

print("\nChecking if empty browsing session with 'not browing_session'")
print("Empty? " + str(not browsing_session))
if not browsing_session:
    print("disable")
    print(browsing_session[-1])

if browsing_session:
    print("\nIF statement: Checking 'if browsing_session' i.e. is is true/not empty")
    print(browsing_session)
