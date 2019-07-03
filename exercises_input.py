#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/

# Make a program that asks a phone number.
check = True
while check:
    phonenumber = input("Please provide a phone number: ")
    if phonenumber.isdigit():
        print("Your phone number is : " + str(phonenumber))
        check = False
    else:
        print("Sorry, only whole numbers accepted" + "\n")

# Make a program that asks the users preferred programming language.

check = True

while check:
    preferredlang = input(
        "\nUsing characters only, please input your preferred programming language: ")
    for char in preferredlang:
        if not char.isalpha():
            check = False
    if check:
        print("Your preference is: " + preferredlang)
        break
    else:
        print("Only characters allowed, goodbye! \n")
