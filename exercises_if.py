#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/


# Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.
answer = input("Please input a number between 1 and 10: ")

if 1 <= int(answer) <= 10 and answer.isdigit:
    print("Your number was " + str(answer))
else:
    print("Invalid number received\n")

# Make a program that asks a password.
mypassword = input("Please provide your password: ")

if str(mypassword) is None:
    print("Invalid input received")
else:
    print("Your password was accepted")
