"""
write a prgram that can store and manipulate rectangles and points.
points should store x and y coordinates
rectangels should store their top left point, then a w for width and an h for height
Both should have __repr__ and __eq__ implemented
"""

import math


class Point(object):

    def __init__(self, x, y):
        """
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={}, y={}".format(self.x, self.y)

    def __eq__(self, other):
        samex = self.x == other.x
        samey = self.y == other.y
        same = samex and samey
        return same

    def __sub__(self, other):
        """
        diffx is the new x coordinate minus the old x coordinate
        diffy is the new y coordinate minus the old y coordinate
        :param other: new x and y coordinates
        :return: dist is the distance between the two points, the Pythagorean equation
        """
        diffx = other.x - self.x
        diffy = other.y - self.y
        dist = sqrt(diffx**2 + diffy**2)
        return dist

    def move(self, x, y):
        """
        Making a new point
        :param x: old x coordinate
        :param y: old y coordinate
        :return:
        """
        newx = self.x + x
        newy = self.y + y
        return Point(newx, newy)


    #point = \

    Point(x, y)
    point(2,5)

