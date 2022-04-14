"""
Name: Scarlett Duncan
lab12.py

Problem: write a program that practices using list manipulation and while loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    if list.count(value) != 0:
        position = list.index(value)
        list.insert(position, "Scarlett")
        list.remove(value)


def good_input():
    good_input_question = False
    good_input = eval(input("Enter a good input from 1-10: "))
    while not good_input_question:
        if good_input < 1:
            good_input = eval(input("Your input was too low. Enter a number from 1-10: "))
        elif good_input > 10:
            good_input = eval(input("Your input was too high. Enter a number from 1-10: "))
        elif 1 <= good_input <= 10:
            return good_input


def num_digits():
    i = 1
    count_divisions = 0
    while i > 0:
        i = eval(input("Enter an integer (end with 0 or negative)"))
        new_i = i
        while new_i != 0:
            new_i = new_i // 10
            count_divisions = count_divisions + 1
        print("the number of digits is {}".format(count_divisions))
        count_divisions = 0


def hi_lo_game():
    i = 0
    rand_num = randint(1, 100)
    guess = eval(input("Guess a number from 1-100"))
    guess_right = False
    while not guess_right:
        i = i + 1
        if i < 7:
            if guess < rand_num:
                guess = eval(input("That's too low. Guess another number from 1-100"))
            elif guess > rand_num:
                guess = eval(input("That's too high. Guess another number from 1-100"))
            elif guess == rand_num:
                print("You win in {} guesses!".format(i))
                guess_right = True
        else:
            print("Sorry, you lose. The number was {}".format(rand_num))
            guess_right = True
