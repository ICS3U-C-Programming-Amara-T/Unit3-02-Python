#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 18, 2025

# In this code the user will guess the number.
import constants


def main():
    # Enter a number between 15 and 107
    user_guess = int(input("Enter your number guess: "))
    print("")

    # Check the user guess is correct
    if user_guess != constants.CORRECT_GUESS:
        print("Wrong number! ")

    # Check if the user guess is wrong
    if user_guess == constants.CORRECT_GUESS:
        print("Correct Answer!")


if __name__ == "__main__":
    main()
