#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program loops to find factorial of a number

import string


def main():
    # This function gets the factorial of a number

    # Input
    input_as_string = str(input("Enter a positive integer: "))
    loop_counter = 0
    total = 1

    # Process and Output
    try:
        input_as_integer = int(input_as_string)
        if input_as_integer >= 0:
            while loop_counter < input_as_integer:
                loop_counter = loop_counter + 1
                total = total * loop_counter
            print("\n{}! = {}".format(input_as_string, total))
        else:
            print("\n{} is not a positive integer".format(input_as_string))

    except Exception:
        print("\n{} is not a positive integer".format(input_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
