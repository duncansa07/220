"""
Name: Scarlett Duncan
lab6.py

Problem: Create a program that will allow a user to enter a message and a keyword, then will encode it.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


def vigenere():
    win = GraphWin("Vigenere", 600, 300)
    button = Rectangle(Point(250, 175), Point(350, 225))
    button.draw(win)
    center = button.getCenter()
    encode = Text(center, "Encode")
    encode.draw(win)
    enter_message = Entry(Point(375, 30), 45)
    message_text = Text(Point(75, 30), "Message to code")
    enter_message.draw(win)
    message_text.draw(win)
    enter_key = Entry(Point(260, 80), 20)
    key_text = Text(Point(80, 80), "Enter keyword")
    enter_key.draw(win)
    key_text.draw(win)
    win.getMouse()
    button.undraw()
    encode.undraw()

    text_message = enter_message.getText()
    text_key = enter_key.getText()
    text_message_upper = text_message.upper()
    message_cleaned = text_message_upper.replace(" ", "")
    text_key = text_key.upper()
    text_key = text_key.replace(" ", "")
    length_key = len(text_key)

    output = ""
    length = len(message_cleaned)
    for i in range(length):
        step_1 = ord(message_cleaned[i]) - 65
        step_2 = ord(text_key[i % length_key]) - 65
        step_3 = step_1 + step_2
        step_4 = (step_3 % 26) + 65
        fin = chr(step_4)
        output = output + fin
    message = "Resulting Message\n" + output
    result = Text(Point(300, 200), message)
    result.draw(win)
    close = Text(Point(300, 275), "Click Anywhere to Close Window")
    close.draw(win)
    win.getMouse()
    win.close()

