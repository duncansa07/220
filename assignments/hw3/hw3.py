"""
Name: Scarlett Duncan
hw3.py

Problem: Create a program that uses loops for various problems

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke Duvall (CSL)
"""


def average():
    amt_grades = eval(input("how many grades will you enter?"))
    add_grade = 0
    for _ in range(amt_grades):
        new_grade = eval(input("Enter grade:"))
        add_grade = add_grade + new_grade
    avg_grade = add_grade / amt_grades
    round(avg_grade, 1)
    print("average is ", avg_grade)


def tip_jar():
    tip_add = 0
    for _ in range(5):
        tip_amt = eval(input("how much would you like to donate?"))
        tip_add = tip_amt + tip_add
    print("total tips:", tip_add)


def newton():
    sqr_root = eval(input("What number do you want to square root?"))
    approx = sqr_root
    improve = eval(input("How many times should we improve the approximation?"))
    for _ in range(improve):
        approx = (approx + (sqr_root/approx))/2
    print("the square root is approximately", approx)


def sequence():
    numb_terms = eval(input("how many terms would you like?"))
    for i in range(-1, numb_terms-1):
        print(i + (i % 2)+1, end=" ")


def pi():
    numb_terms = eval(input("how many terms in the series?"))
    prod = 1
    for i in range(numb_terms):
        num = ((i-1) % 2) + i + 1
        den = i + (i % 2) + 1
        prod = prod * float(num) / float(den)
    print(prod * 2)


if __name__ == '__main__':
    pass
