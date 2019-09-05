#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781751

# xxargs pass in arbitrary number of Key Value pairs (keyword arguments)
# aka kwargs!

#  first exercise
print("first - xxargs pass in arbitrary number of Key Value pairs:")


def saveuser(**user):
    print(user)


saveuser(id=1, name="Theresa")

# second exercise
print("second - print one of the pairs passed in:")

# asterisk before parameter makes the parameter a tuple


def saveuser2(**user):
    print(user["id"])


saveuser2(id=1, name="Theresa")


#  third exercise
print("third - can I pass in multiple records?:")


def saveuser3(**user):
    print(user)


saveuser3(id=1, name="Theresa")
saveuser3(id=2, name="John")

print("verdict - not really, only new records overwriting last")
