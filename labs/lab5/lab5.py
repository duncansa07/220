"""
Name: Scarlett Duncan
lab5.py

Problem: Create codes that draw various graphics using the graphics module and practices using strings

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
from math import *


def triange():
    win = GraphWin("Triangle", 400, 400)
    instruction_1 = Text(Point(200, 10), "Click 3 corners of triangle")
    instruction_1.draw(win)
    corner_1 = win.getMouse()
    corner_2 = win.getMouse()
    corner_3 = win.getMouse()
    instruction_1.undraw()
    x_1 = corner_1.getX()
    x_2 = corner_2.getX()
    x_3 = corner_3.getX()
    y_1 = corner_1.getY()
    y_2 = corner_2.getY()
    y_3 = corner_3.getY()
    triangle = Polygon(Point(x_1, y_1), Point(x_2, y_2), Point(x_3, y_3))
    triangle.draw(win)
    dx1 = x_1 - x_2
    dy1 = y_1 - y_2
    dx2 = x_2 - x_3
    dy2 = y_2 - y_3
    dx3 = x_3 - x_1
    dy3 = y_3 - y_1
    length_1 = sqrt((dx1 ** 2) + (dy1 ** 2))
    length_2 = sqrt((dx2 ** 2) + (dy2 ** 2))
    length_3 = sqrt((dx3 ** 2) + (dy3 ** 2))
    perimeter = length_1 + length_2 + length_3
    perimeter_text = "The perimeter is: " + str(perimeter)
    area = (length_1 + length_2 + length_3)/2
    area_text = "The area is: " + str(area)
    perimeter_display = Text(Point(200, 10), perimeter_text)
    area_display = Text(Point(200, 30), area_text)
    perimeter_display.draw(win)
    area_display.draw(win)
    close = Text(Point(200, 190), "Click to close")
    close.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    for i in range(5):
        # create text instructions
        msg = "Enter color values between 0 - 255\nClick window to color shape"
        inst = Text(Point(win_width / 2, win_height - 20), msg)
        inst.draw(win)

        # add entry boxes
        input_green = Entry(Point(200, 200), 10)
        input_green.draw(win)
        input_red = Entry(Point(200, 100), 10)
        input_red.draw(win)
        input_blue = Entry(Point(200, 300), 10)
        input_blue.draw(win)
        win.getMouse()
        input_blue.undraw()
        input_red.undraw()
        input_green.undraw()
        inst.undraw()

        #change entries into strings
        red = eval(input_red.getText())
        green = eval(input_green.getText())
        blue = eval(input_blue.getText())

        # create circle in window's center
        shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
        shape.setFill(color_rgb(red, green, blue))
        shape.draw(win)

        # redTexPt is 50 pixels to the left and forty pixels down from center
        red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
        red_text = Text(red_text_pt, "Red: " + str(red))
        red_text.setTextColor("red")

        # green_text_pt is 30 pixels down from red
        green_text_pt = red_text_pt.clone()
        green_text_pt.move(0, 30)
        green_text = Text(green_text_pt, "Green: " + str(green))
        green_text.setTextColor("green")

        # blue_text_pt is 60 pixels down from red
        blue_text_pt = red_text_pt.clone()
        blue_text_pt.move(0, 60)
        blue_text = Text(blue_text_pt, "Blue: " + str(blue))
        blue_text.setTextColor("blue")

        # display rgb text
        red_text.draw(win)
        green_text.draw(win)
        blue_text.draw(win)

        #run through again
        again = Text(Point(200, 390), "Click to choose another combination")
        again.draw(win)
        win.getMouse()
        red_text.undraw()
        blue_text.undraw()
        green_text.undraw()
        shape.undraw()
        again.undraw()

    # Wait for another click to exit
    close = Text(Point(200, 390), "Click to Close")
    close.draw(win)
    win.getMouse()
    win.close()


def process_string():
    string = input("Input a string ")

    a = string[0]
    print(a)

    b = string[len(string) - 1]
    print(b)

    c = string[1:5]
    print(c)

    d = a + b
    print(d)

    e = string[:3]
    print(e * 10)

    loop_range = len(string)

    for i in range(loop_range):
        f = string[i]
        print(f)

    g = len(string)
    print(g)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * values[0]
    print(x)

    x = values[2:5]
    print(x)

    x = values[2:4]
    x.append(values[0])
    print(x)

    x = values[2:3]
    x.append(values[0])
    x.append(eval(values[5]))
    print(x)

    x = values[0] + values[2] + eval(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(terms):
        series_basic = i % 3
        series_actual = series_basic * 2 + 2
        acc = acc + series_actual
        print(series_actual, end="")
    print("\nSum = ", acc)



def target():
    win = GraphWin("Archery Target", 100, 100)
    white_circle = Circle(Point(50, 50), 50)
    white_circle.setFill("white")
    white_circle.draw(win)
    black_circle = Circle(Point(50, 50), 40)
    black_circle.setFill("black")
    black_circle.draw(win)
    blue_circle = Circle(Point(50, 50), 30)
    blue_circle.setFill("blue")
    blue_circle.draw(win)
    red_circle = Circle(Point(50, 50), 20)
    red_circle.setFill("red")
    red_circle.draw(win)
    yellow_circle = Circle(Point(50, 50), 10)
    yellow_circle.setFill("yellow")
    yellow_circle.draw(win)
    close = Text(Point(50, 50), "Click to Close")
    close.draw(win)
    win.getMouse()
    win.close()
