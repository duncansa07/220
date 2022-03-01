"""
Name: Scarlett Duncan
lab7.py
Problem: Create a simulation of bumper cars using a variety of functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *
from math import *


def get_random(move_amt):
    rand_int = randint((-1 * move_amt), move_amt)
    return rand_int


def did_collide(circle_ball, circle_ball_2):
    radius_1 = circle_ball.getRadius()
    radius_2 = circle_ball_2.getRadius()
    center_1 = circle_ball.getCenter()
    x_1 = center_1.getX()
    y_1 = center_1.getY()
    center_2 = circle_ball_2.getCenter()
    x_2 = center_2.getX()
    y_2 = center_2.getY()
    distance = sqrt(((x_2 - x_1) * (x_2 - x_1)) + ((y_2 - y_1) * (y_2 - y_1)))
    radius_add = radius_2 + radius_1
    return distance <= radius_add


def hit_vertical(circle_ball, win):
    win_height = win.getHeight()
    radius = circle_ball.getRadius()
    center = circle_ball.getCenter()
    center_y = center.getY()
    distance = radius + center_y
    distance_negative = center_y - radius
    return distance >= win_height or distance_negative <= 0


def hit_horizontal(circle_ball, win):
    win_width = win.getWidth()
    radius = circle_ball.getRadius()
    center = circle_ball.getCenter()
    center_x = center.getX()
    distance = radius + center_x
    distance_negative = center_x - radius
    return distance_negative <= 0 or distance >= win_width


def get_random_color():
    ran_color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return ran_color


def bumper():
    win = GraphWin("Bumper", 400, 400)
    circle_1 = Circle(Point(randint(0, 400), randint(0, 400)), 20)
    circle_2 = Circle(Point(randint(0, 400), randint(0, 400)), 20)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)

    move_amt = 20
    circle_1_x_move = get_random(move_amt)
    circle_1_y_move = get_random(move_amt)
    circle_2_x_move = get_random(move_amt)
    circle_2_y_move = get_random(move_amt)
    while not win.checkMouse():
        circle_1.move(circle_1_x_move, circle_1_y_move)
        circle_2.move(circle_2_x_move, circle_2_y_move)
        time.sleep(0.5)
        if did_collide(circle_1, circle_2):
            circle_1_x_move = -circle_1_x_move
            circle_1_y_move = -circle_1_y_move
            circle_2_x_move = -circle_2_x_move
            circle_2_y_move = -circle_2_y_move
            circle_1.move(circle_1_x_move, circle_1_y_move)
            circle_2.move(circle_2_x_move, circle_2_y_move)
        if hit_horizontal(circle_1, win):
            circle_1_x_move = -circle_1_x_move
            circle_1.move(circle_1_x_move, circle_1_y_move)
        if hit_horizontal(circle_2, win):
            circle_2_x_move = -circle_2_x_move
            circle_2.move(circle_2_x_move, circle_2_y_move)
        if hit_vertical(circle_1, win):
            circle_1_y_move = -circle_1_y_move
            circle_1.move(circle_1_x_move, circle_1_y_move)
        if hit_vertical(circle_2, win):
            circle_2_y_move = -circle_2_y_move
            circle_2.move(circle_2_x_move, circle_2_y_move)
    win.close()
