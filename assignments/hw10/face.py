"""
Name: Scarlett Duncan
face.py

Problem: modify the class face to create 3 other face expressions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_center = self.mouth.getCenter()
        mouth_center_clone = mouth_center.clone()
        mouth_center_clone.move(0, mouth_center/2)
        mouth_p1 = self.mouth.getP1()
        mouth_p2 = self.mouth.getP2()
        smile_side_1 = Line(mouth_p1, mouth_center_clone)
        smile_side_2 = Line(mouth_p2, mouth_center_clone)
        smile_side_1.draw(self.window)
        smile_side_2.draw(self.window)

    def shock(self):
        circle_center = self.mouth.getCenter()
        mouth_shocked = self.left_eye.clone()
        mouth_shocked.move(circle_center)
        mouth_shocked.draw(self.window)

    def wink(self):
        mouth_center = self.mouth.getCenter()
        mouth_center_clone = mouth_center.clone()
        mouth_center_clone.move(0, mouth_center / 2)
        mouth_p1 = self.mouth.getP1()
        mouth_p2 = self.mouth.getP2()
        smile_side_1 = Line(mouth_p1, mouth_center_clone)
        smile_side_2 = Line(mouth_p2, mouth_center_clone)
        smile_side_1.draw(self.window)
        smile_side_2.draw(self.window)

        eye_center = self.left_eye.getCenter()
        eye_y = eye_center.getY()
        eye_x = eye_center.getX()
        eye_radius = self.left_eye.getRadius()
        line_x1 = eye_x - eye_radius
        line_x2 = eye_x + eye_radius
        self.left_eye.undraw()
        eye_line = Line(Point(line_x1, eye_y), Point(line_x2, eye_y))
        eye_line.draw(self.window)

