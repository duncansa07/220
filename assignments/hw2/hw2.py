"""
Name: Scarlett Duncan
hw2.py

Problem: This program is designed to perform various arithmatic problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    acc_threes = 0
    for i in range(0, upper_bound+1, 3):
        acc_threes = acc_threes + i
    print(acc_threes)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            multiplication = i * j
            print(multiplication, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    sides = (side_a + side_b + side_c) / 2
    area = math.sqrt(sides * (sides - side_a) * (sides - side_b) * (sides - side_c))
    print("area is ", area)


def sum_squares():
    lower_limit = eval(input("Enter lower range: "))
    upper_limit = eval(input("Enter upper range: "))
    acc_squares = 0
    for i in range(lower_limit, upper_limit+1):
        acc_squares = (i * i) + acc_squares
    print(acc_squares)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    acc_power = 1
    for _ in range(exponent):
        acc_power = base * acc_power
    print(base, "^", exponent, "=", acc_power)


if __name__ == '__main__':
    pass
