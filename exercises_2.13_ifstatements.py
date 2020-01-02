#!/usr/bin/env python3
# https://pythonbasics.org/exercises/
# If statements

# Make a program that asks the number between 1 and 10.
# If the number is out of range the program should display “invalid number”.

num = input("Enter a number between 1 and 10: ")

if num.isnumeric() and int(num) in range(1, 10):
    print("Valid input: " + str(num))
else:
    print("Invalid input received")

# Make a program that asks a password.
mypassword = input("Please provide your password: ")

if str(mypassword) is "":
    print("Invalid input received")
else:
    print("Your password was accepted")
