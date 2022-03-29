"""
Name: Scarlett Duncan
button.py

Problem: Write a code that uses classes you create to draw a door that opens and closes with a click

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        point_1 = self.shape.getP1()
        point_2 = self.shape.getP2()
        x_1 = point_1.getX()
        x_2 = point_2.getX()
        y_1 = point_1.getY()
        y_2 = point_2.getY()
        x_value = point.getX()
        y_value = point.getY()
        if (x_1 <= x_value <= x_2) and (y_1 <= y_value <= y_2):
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)


