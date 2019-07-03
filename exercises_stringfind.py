#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/

# Find out if string find is case sensitive
# s = "That I ever did see. Dusty as the handle on the door"

# index = s.find("Dusty")
# print(index)

# if "Dusty" in s:
#     print("query found")

# # What if a query string appears twice in the string?
# s = "That I ever did see. Dusty Dusty as the handle on the door"

# index = s.find("Dusty")
# print(index)


# Write a program that asks console input and searches for a query.
phrase = input("Please type in a phrase: ")
search = input("What word are we searching for? ")
output = phrase.find(search)
print(output)
if(output >= 0):
    print("You searched for " + search +
          " and we found it at index " + str(output))
else:
    print("Your string was not found")
