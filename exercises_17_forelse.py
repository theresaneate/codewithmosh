#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781757

# Theresa's notes: else with for = aka "no break"

names = ["AJohn", "Mary"]
found = False

for name in names:
    if name.startswith("J"):
        print("\nFound!")
        # found = True
        break

else:
    print("\nNot found")


# =====================================
# bad example
# my_list = [1, 2, 3, 4, 5]

# for i in my_list:
#     print(i)
#     break
# else:
#     print("Hit the for/else statement")
# =====================================


# better example
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


my_list = ["Corey", "Rick", "John"]
name = input("What name do you want to find? ")
index_location = find_index(my_list, name)
if index_location != -1:
    print("Location of target is index: {}".format(index_location))
else:
    my_list.append(name)
    print("New name added to list")

for name in my_list:
    print(name)
