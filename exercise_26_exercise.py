#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781741

# fizzbuzz
# 3 = fizz
# 5 = buzz

stringinput = input("Please provide a number: ")
myinput = float(stringinput)


def fizzbuzz(myinput):
    print("input / 3 = " + str(myinput/3))
    print("input / 5 = " + str(myinput/5))
    if (myinput % 3 == 0.0 and myinput % 5 == 0.0):
        print("FizzBuzz")
    elif myinput % 3 == 0:
        print("Fizz")
    elif myinput % 5 == 0:
        print("Buzz")
    else:
        print("Nothing Fizzy or Buzzy here")


fizzbuzz(int(myinput))
