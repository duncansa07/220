"""
Name: Scarlett Duncan
lab11.py

Problem: write a program that creates a three door game using classes

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.door import Door
from graphics import *
from lab10.button import Button
from random import randint


def main():
    shape_button = Rectangle(Point(450,25), Point(550, 100))
    win = GraphWin("Three Door Game", 600, 600)
    win.setBackground("RoyalBlue")
    button = Button(shape_button, "Quit")
    button.draw(win)

    shape_door_1 = Rectangle(Point(75, 200), Point(200, 450))
    shape_door_1.setFill("SaddleBrown")
    shape_door_2 = Rectangle(Point(250, 200), Point(375, 450))
    shape_door_2.setFill("SaddleBrown")
    shape_door_3 = Rectangle(Point(425, 200), Point(550, 450))
    shape_door_3.setFill("SaddleBrown")
    door_1 = Door(shape_door_1, "Door 1")
    door_2 = Door(shape_door_2, "Door 2")
    door_3 = Door(shape_door_3, "Door 3")
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    words = Text(Point(300, 150), "I have a secret door")
    words.draw(win)
    instructions = Text(Point(300, 525), "Click to guess which is the secret door!")
    instructions.draw(win)

    win_box = Rectangle(Point(50, 25), Point(125, 100))
    losses_box = Rectangle(Point(125, 25), Point(200, 100))
    win_box.draw(win)
    losses_box.draw(win)
    win_text = Text(Point(85, 15), "wins")
    loss_text = Text(Point(165, 15), "losses")
    win_text.draw(win)
    loss_text.draw(win)
    win_mid = win_box.getCenter()
    lose_mid = losses_box.getCenter()
    win_number = Text(win_mid, "0")
    loss_number = Text(lose_mid, "0")
    win_number.draw(win)
    loss_number.draw(win)

    door_numb = randint(1, 3)
    if door_numb == 1:
        door_1.set_secret(True)
        secret_door = door_1
    elif door_numb == 2:
        secret_door = door_2.set_secret(True)
        secret_door = door_2
    else:
        secret_door = door_3.set_secret(True)
        secret_door = door_3

    wins = 0
    losses = 0
    game_end = False
    user_click = win.getMouse()
    while not game_end:
        if button.is_clicked(user_click):
            game_end = True
            win.close()
        if secret_door.is_clicked(user_click):
            secret_door.color_door("green")
            words.undraw()
            win_message = Text(Point(300, 150), "you win!")
            win_message.draw(win)
            instructions.undraw()
            new_instructions = Text(Point(300, 525), "click anywhere to play again")
            new_instructions.draw(win)
            wins = wins + 1
            win_number.undraw()
            win_number = Text(win_mid, "{}".format(wins))
            win_number.draw(win)
            reset = win.getMouse()
            if button.is_clicked(reset):
                game_end = True
                win.close()
            else:
                door_numb = randint(1, 3)
                if door_numb == 1:
                    door_1.set_secret(True)
                    secret_door = door_1
                elif door_numb == 2:
                    secret_door = door_2.set_secret(True)
                    secret_door = door_2
                else:
                    secret_door = door_3.set_secret(True)
                    secret_door = door_3
                door_1.color_door("SaddleBrown")
                door_2.color_door("SaddleBrown")
                door_3.color_door("saddlebrown")
                new_instructions.undraw()
                win_message.undraw()
                instructions.draw(win)
                words.draw(win)
        else:
            if door_1.is_clicked(user_click):
                not_secret_door = door_1
            elif door_2.is_clicked(user_click):
                not_secret_door = door_2
            else:
                not_secret_door = door_3

            secret_door.color_door("green")
            not_secret_door.color_door("red")
            words.undraw()
            instructions.undraw()
            loss_message = Text(Point(300, 150), "sorry, incorrect!")
            new_instructions = Text(Point(300, 525), "click anywhere to play again")
            loss_message.draw(win)
            new_instructions.draw(win)
            loss_number.undraw()
            losses = losses + 1
            loss_number = Text(lose_mid, "{}".format(losses))
            loss_number.draw(win)
            reset = win.getMouse()
            if button.is_clicked(reset):
                game_end = True
                win.close()
            else:
                door_numb = randint(1, 3)
                if door_numb == 1:
                    door_1.set_secret(True)
                    secret_door = door_1
                elif door_numb == 2:
                    secret_door = door_2.set_secret(True)
                    secret_door = door_2
                else:
                    secret_door = door_3.set_secret(True)
                    secret_door = door_3
                door_1.color_door("SaddleBrown")
                door_2.color_door("SaddleBrown")
                door_3.color_door("SaddleBrown")
                new_instructions.undraw()
                loss_message.undraw()
                instructions.draw(win)
                words.draw(win)
        user_click = win.getMouse()
