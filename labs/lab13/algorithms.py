"""
Name: Scarlett Duncan
algorithms.py

Problem: write a program that practices using while loops to read files and sort lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Rectangle, Point


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


def selection_sort(values):
    unsorted_position_start = 0
    while unsorted_position_start < len(values):
        min = unsorted_position_start
        for i in range(unsorted_position_start, len(values)):
            if values[i] < values[min]:
                min = i
        values[min], values[unsorted_position_start] = values[unsorted_position_start], values[min]
        unsorted_position_start = unsorted_position_start + 1


def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    x_1 = point_1.getX()
    x_2 = point_2.getX()
    y_1 = point_1.getY()
    y_2 = point_2.getY()
    length = abs(x_2 - x_1)
    height = abs(y_2 - y_1)
    area = length * height
    return area


def rect_sort(rectangles):
    unsorted_rec_pos = 0
    while unsorted_rec_pos < len(rectangles):
        min = unsorted_rec_pos
        for i in range(unsorted_rec_pos, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[min]):
                min = i
        rectangles[min], rectangles[unsorted_rec_pos] = rectangles[unsorted_rec_pos], rectangles[min]
        unsorted_rec_pos = unsorted_rec_pos + 1

