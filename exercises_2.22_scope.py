#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781740

# global vs local/function scope

# global var below
message = "b"


def greet():
    message = "a"
    return message


print("will return local variable: ")
print(greet())


# global var below
message = "b"


def greet2():
    message = "a"
    print("from within the function:")
    print(message)


print("will return local A variable: ")
greet2()

print("before messing with global/local from outside the function, return global B:")
print(message)


# assigning global to local var
def greet3():
    global message
    message = "c"
    print("from within the function:")
    print(message)


print("running function will return global - BAD! - variable: ")
greet3()

print("output value of MESSAGE, from outside the function:")
print(message)
