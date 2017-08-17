"""
write a prgram that can store and manipulate rectangles and points.
points should store x and y coordinates
rectangels should store their top left point, then a w for width and an h for height
Both should have __repr__ and __eq__ implemented
"""

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

    point = Point(x, y)
    point(2,5)


class Rectangle(object):

    def __init__(self, tlp, w, h):
        """
        :param tlp: top left point
        :param w: width
        :param h: height
        """
        self.tlp = tlp
        self.w = w
        self.h = h

    def __repr__(self):
        pass

