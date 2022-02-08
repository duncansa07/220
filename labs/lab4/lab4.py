"""
Name: Scarlett Duncan
lab4.py
Problem: Create an animated Valentine's Day greeting card using graphics and loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


def greeting_card():
    win = GraphWin("Valentines Card", 500, 700)
    win.setCoords(100, 150, 0, 0)
    win.setBackground("pink")
    heart = Polygon(Point(50, 40), Point(70, 20), Point(90, 50), Point(50, 100), Point(10, 50), Point(30, 20))
    heart.setFill("crimson")
    heart.setOutline("dark red")
    heart.setWidth(4)
    heart.draw(win)
    greeting = Text(Point(50, 125), "Happy\n Valentine's Day!")
    greeting.setTextColor("medium violet red")
    greeting.setSize(36)
    greeting.setFace("helvetica")
    greeting.setStyle("bold")
    greeting.draw(win)
    line_1 = Line(Point(100, 85), Point(80, 75))
    line_1.setArrow("last")
    line_1.setWidth(3)
    line_1.draw(win)
    for i in range(5):
        line_1.move(-20, -10)
        time.sleep(1)
    good_bye = Text(Point(50, 140), "Click anywhere to close")
    good_bye.draw(win)
    win.getMouse()
    win.close()
