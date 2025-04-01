#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 28, 2025
# This program casts a string to an integer
# then asks the user to enter their age and the program
# tells you if you can date their grandchild.


def main():
    # Get the user's age
    age_string = input("Enter your age: ")

    # CAST a string into an integer
    try:
        age_integer = int(age_string)
        if age_integer > 25 and age_integer < 40:
            print(
                "You are of age, you can date my grandchild !"
            )  # The output if the user meets the age standards
        else:
            print(
                "You are too young, you absolutely cannot date my grandchild"
            )  # The output if the user doesn't meet the age standards
    except Exception:
        print(
            "{} is not a number".format(age_string)
        )  # The output if user doesn't input a number
    finally:
        print("Thank you for playing")  # This displays regardless


if __name__ == "__main__":
    main()
