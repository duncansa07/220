"""
Name: Scarlett Duncan
hw4.py

Problem: Create codes that draw various graphics using the graphics module.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from math import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to Draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()

        # move amount is distance from center of circle to the
        # point where the user clicked
        new_p1 = Point(click.getX() - 25, click.getY() - 25)
        new_p2 = Point(click.getX() + 25, click.getY() + 25)
        new_rectangle = Rectangle(new_p1, new_p2)
        new_rectangle.setOutline("red")
        new_rectangle.setFill("red")
        new_rectangle.draw(win)
    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    text_1 = Text(Point(200, 10), "Click corner 1")
    text_1.draw(win)
    corner_1 = win.getMouse()
    text_1.undraw()
    text_2 = Text(Point(200, 10), "Click opposite corner")
    text_2.draw(win)
    corner_2 = win.getMouse()
    text_2.undraw()
    x_1 = corner_1.getX()
    y_1 = corner_1.getY()
    x_2 = corner_2.getX()
    y_2 = corner_2.getY()
    rectangle = Rectangle(Point(x_1, y_1), Point(x_2, y_2))
    rectangle.setFill("green")
    rectangle.setOutline("black")
    rectangle.draw(win)
    height = abs(y_1 - y_2)
    width = abs(x_1 - x_2)
    perimeter = width * 2 + height * 2
    area = height * width
    perim = "perimeter:", perimeter
    ar = "Area:", area
    text_per = Text(Point(200, 370), perim)
    text_area = Text(Point(200, 390), ar)
    text_per.draw(win)
    text_area.draw(win)
    close = Text(Point(200, 10), "Click to Close")
    close.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    text_center = Text(Point(200, 390), "Click the center of the circle")
    text_center.draw(win)
    center = win.getMouse()
    text_center.undraw()
    text_radius = Text(Point(200, 390), "Click for the radius of the Circle")
    text_radius.draw(win)
    radius = win.getMouse()
    text_radius.undraw()
    x_1 = center.getX()
    x_2 = radius.getX()
    y_1 = center.getY()
    y_2 = radius.getY()
    distance = sqrt(pow((x_2 - x_1), 2) + pow((y_2 - y_1), 2))
    circle = Circle(center, distance)
    circle.setFill("light blue")
    circle.setOutline("black")
    circle.draw(win)
    dist = "Radius:", distance
    distance_text = Text(Point(200, 390), dist)
    distance_text.draw(win)
    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("enter the number of terms to sum:"))
    pi_approx = 0
    numerator = 4
    denominator = 1
    sign = 1
    for i in range(terms):
        series = (numerator / denominator) * sign
        denominator = denominator + 2
        sign = sign * (-1)
        pi_approx = pi_approx + series
    difference = abs(pi - pi_approx)
    print("Pi approximation:", pi_approx)
    print("accuracy:", difference)


if __name__ == '__main__':
    pass
