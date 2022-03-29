"""
Name: Scarlett Duncan
lab10.py

Problem: Write a code that uses classes you create to draw a door that opens and closes with a click

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from button import Button
from door import Door

def main():
    shape_button = Rectangle(Point(100, 10), Point(300, 100))
    win = GraphWin("Test", 400, 700)
    button = Button(shape_button, "Exit")
    button.draw(win)

    shape_door = Rectangle(Point(100, 120), Point(300, 650))
    door = Door(shape_door, "Closed")
    door.color_door("red")
    door.draw(win)

    user_click = win.getMouse()
    while not button.is_clicked(user_click):
        if button.is_clicked(user_click):
            win.close()
        if door.is_clicked(user_click):
            if not door.is_secret():
                door.open("white", "Open")
                door.set_secret(True)
            elif door.is_secret():
                door.close("red", "Closed")
                door.set_secret(False)
        user_click = win.getMouse()


