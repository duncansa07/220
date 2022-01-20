"""
Name: Scarlett Duncan
hw1.py

Problem: We are using this code to practice using arithmatic and inputs to create outputs.
It is used as an overview of using pycharm and pushing to gitHub.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    made_shots = eval(input("Enter how many shots the player made: "))
    shot_percentage = (made_shots/total_shots) * 100
    print("Shooting Percentage: ", shot_percentage, "%")


def coffee():
    amt_coffee = eval(input("How many pounds of coffee would you like?"))
    shipping_total = (amt_coffee * 10.5) + (amt_coffee * .86) + 1.5
    print("Your total is: $", shipping_total)


def kilometers_to_miles():
    km_traveled = eval(input("How many kilometers did you travel?"))
    miles_traveled = km_traveled/1.61
    print("That's", miles_traveled, "miles!")


if __name__ == '__main__':
    pass
