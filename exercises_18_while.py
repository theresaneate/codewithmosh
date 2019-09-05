#!/usr/bin/env python3
# https://codewithmosh.com/courses/423295/lectures/6781749

import random

guess = 0
answer = random.randint(1, 5)
# print(answer)

while answer != guess:
    guess = int(input("Guess the number from 1 to 5: "))
    if guess not in range(1, 6) or guess is False:
        print("Only values between 1 and 5 are accepted")
else:
    print("You guessed the right number: " + str(answer))
