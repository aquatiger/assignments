"""
write a prgram that can store and manipulate rectangles and points.
points should store x and y coordinates
rectangels should store their top left point, then a w for width and an h for height
Both should have __repr__ and __eq__ implemented
"""

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
