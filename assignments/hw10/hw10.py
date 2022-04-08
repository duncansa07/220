"""
Name: Scarlett Duncan
hw10.py

Problem: create a series of functions that practices using while loops, booleans, and classes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(n):
    list = [0, 1]
    if n < 1:
        return None
    else:
        while len(list) <= n:
            list.append(list[-1] + list[-2])
        return list[-1]


def double_investment(principle, rate):
    double = principle * 2
    principle = principle
    year = 0
    while principle < double:
        principle = principle * (1 + rate)
        year = year + 1
    return year


def syracuse(n):
    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
            list.append(n)
        elif n % 2 == 1:
            n = (3 * n) + 1
            list.append(n)
    return list

def goldbach(n):
    pass
