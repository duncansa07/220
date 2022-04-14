"""
Name: Scarlett Duncan
algorithms.py

Problem: write a program that practices using while loops to read files.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def read_data(filename):
    file = open(filename, "r")
    list_file = []
    line = file.readline()
    while line:
        line_cleaned = line.replace("\n", "")
        line_better = line_cleaned.split(' ')
        i = 0
        line_best = []
        while i < len(line_better):
            num = eval(line_better[i])
            line_best.append(num)
            i = i + 1
        list_file = list_file + line_best
        line = file.readline()
    file.close()
    return list_file


def is_in_linear(search_val, values):
    i = 0
    true_ask = False
    while i < len(values) and true_ask == False:
        if values[i] == search_val:
            true_ask = True
        else:
            true_ask = False
        i = i + 1
    return true_ask

