"""
Name: Scarlett Duncan
hw8.py

Problem: Create a series of functions to practice using conditionals and control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from math import *
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]


def sum_list(nums):
    sum_nums = 0
    for i in nums:
        sum_nums = i + sum_nums
    return sum_nums


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    new_list = []
    for i in range(len(numbers)):
        nums_split = nums[i].split(", ")
        to_numbers(nums_split)
        square_each(nums_split)
        total = sum_list(nums_split)
        new_list.append(total)
    return new_list


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_2 = Circle(center_2, radius_2)
    circle_2.setFill("light green")
    circle_2.draw(win)
    overlap_text = Text(Point(10, 10), "The circles overlap")
    not_overlap_text = Text(Point(10, 10), "The circles do not overlap")
    if did_overlap(circle_one, circle_2):
        overlap_text.draw(win)
    else:
        not_overlap_text.draw(win)
    close_message = Text(Point(5, 5), "Click to close")

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    radius_one = circle_one.getRadius()
    radius_two = circle_two.getRadius()
    center_one = circle_one.getCenter()
    x_1 = center_one.getX()
    y_1 = center_one.getY()
    center_two = circle_two.getCenter()
    x_2 = center_two.getX()
    y_2 = center_two.getY()
    distance = sqrt(((x_2 - x_1) * (x_2 - x_1)) + ((y_2 - y_1) * (y_2 - y_1)))
    radius_add = radius_two + radius_one
    if distance <= radius_add:
        return True

if __name__ == '__main__':
    pass
