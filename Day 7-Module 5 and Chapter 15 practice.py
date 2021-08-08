# Author: Gan Li
# Date: 8/4/21 7:34 下午 to 8/8/21 4:27 下午
# Description: Module 5 and Chapter 15: Classes and objects
"""
import math


class Point:
    Represents a point in 2-D space.

    def __init__(self, x, y):
        self._x = x
        self._y = y


point = Point()  # Point is a class, point is a class object of the class.
point.x = 3.0
point.y = 4.0  # These elements are called attributes, instead of variables.
pi = math.pi
"""
import math


class HourlyWorker:
    """Represents a work's information"""

    def __init__(self, name, ID, wage):
        self._name = name
        self._ID = ID
        self._wage = wage


class Box:
    """Represents a box"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height


class Circle:
    """Represents a circle"""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_point(point1, point2):
    diff_x = point1.x - point2.x
    diff_y = point1.y - point2.y
    distance = math.sqrt(diff_x ** 2 + diff_y ** 2)
    return distance


def point_in_circle(circle, point):
    return distance_between_point(circle.center, point) <= circle.radius


# 跳过 rect_in_circle and rect_circle_overlap


def main():
    point_x = float(input('Please type in the x-coordinator of the point:'))
    point_y = float(input('Please type in the y-coordinator of the point:'))
    point = Point(point_x, point_y)

    center_x = float(input('Please type in the x-coordinator of circle center:'))
    center_y = float(input('Please type in the y-coordinator of circle center:'))
    circle_center = Point(center_x, center_y)

    circle_radius = float(input('Please type in the radius of the circle'))

    circle = Circle(circle_center, circle_radius)

    print(point_in_circle(circle, point))


if __name__ == '__main__':
    main()
