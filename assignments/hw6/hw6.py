"""
Name: Scarlett Duncan
hw6.py

Problem: Create a program that will use various functions and strings to produce an output.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import pi


def cash_converter():
    integer = eval(input("enter an integer: "))
    print("That is ${}.00".format(integer))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    length = len(message)
    for i in range(length):
        new_numb = ord(message[i]) + key
        new_letter = chr(new_numb)
        print(new_letter, end="")


def sphere_area(radius):
    area = 4 * pi * (radius * radius)
    print("surface area: {}".format(area))


def sphere_volume(radius):
    volume = (4/3) * pi * (radius * radius * radius)
    print("volume: {}".format(volume))


def sum_n(number):
    sum_num = 0
    for i in range(number):
        sum_num = sum_num + i+1
    print("total: {}".format(sum_num))


def sum_n_cubes(number):
    sum_numb = 0
    for i in range(number):
        cube = (i+1) * (i+1) * (i+1)
        sum_numb = sum_numb + cube
    print("total: {}".format(sum_numb))


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    key = key.upper()
    length_message = len(message)
    length_key = len(key)

    for i in range(length_message):
        step_1 = ord(message[i]) - 65
        step_2 = ord(key[i % length_key]) - 65
        step_3 = step_1 + step_2
        step_4 = (step_3 % 26) + 65
        fin = chr(step_4)
        print(fin, end="")


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
