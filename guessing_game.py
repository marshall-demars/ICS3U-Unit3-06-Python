#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program uses if and try statements to guess a random number
#    with user input

import random


def main():
    # this uses if statements to guess a random number

    # input
    random_number = random.randint(1, 9)  # a number between 1 and 9
    user_number_as_string = input("Enter a number between 1 and 10: ")

    # process and output
    try:
        user_number_as_number = int(user_number_as_string)
        if user_number_as_number == random_number:
            print("\nYou guessed correctly!")
        else:
            print("\nYou guessed incorrectly, the number was {}.".format(random_number))
    except ValueError:
        print("\nThis was not an integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
