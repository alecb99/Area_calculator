import math
import numpy as np


class Geometry:
    count = 0

    def __init__(self, name="Shape", points=None):
        self.name = name
        # name is string that is a name of geometry
        self.points = points
        # points are a list of tuple points = [(x0, y0), (x1, y1), ...]
        Geometry.count += 1

    def calculate_area(self):
        pass

    def get_name(self):
        return self.name

    @classmethod
    def count_number_of_geometry(cls):
        return Geometry.count

    def distance(self, index1, index2):
        x1, y1 = self.points[index1]
        x2, y2 = self.points[index2]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return np.sqrt(d2)


class Triangle(Geometry):
    count = 0

    def __init__(self, a, b, c):
        Triangle.count += 1
        super(Triangle, self).__init__("Triangle", [a, b, c])

    def calculate_area(self):
        ab = self.distance(0, 1)
        ac = self.distance(0, 2)
        bc = self.distance(1, 2)
        p = (ab + ac + bc) / 2
        return np.sqrt(p * (p - ab) * (p - ac) * (p - bc))


class Rectangle(Geometry):
    count = 0

    def __init__(self, a, b):
        x1, y1 = a
        x2, y2 = b
        d = b
        b = (x2, y1)
        c = (x1, y2)
        Rectangle.count += 1
        super(Rectangle, self).__init__("Rectangle", [a, b, c, d])

    def calculate_area(self):
        ab = self.distance(0, 1)
        ac = self.distance(0, 2)
        return ab * ac


class Square(Rectangle):
    count = 0

    def __init__(self, a, length):
        x, y = a
        b = (x + length, y - length)
        super(Square, self).__init__(a, b)
        self.name = "Square"

    def calculate_area(self):
        ab = self.distance(0, 1)
        ac = self.distance(0, 2)
        return ab * ac


class Circle(Geometry):
    count = 0

    def __init__(self, o, r):
        self.r = r
        Circle.count += 1
        super(Circle, self).__init__("Circle", [o])

    def calculate_area(self):
        return np.pi * (self.r ** 2)


class Polygon(Geometry):
    count = 0

    def __init__(self, points):
        # Polygon.count += 1
        super(Polygon, self).__init__("Polygon", points)

    def calculate_area(self):
        N = len(self.points)
        S = 0
        for i in range(2, N):
            ab, ac, bc = self.distance(0, i - 1),self.distance(0, i), self.distance(i, i - 1)
            p = (ab + ac + bc) / 2
            S += np.sqrt(p * (p - ab) * (p - ac) * (p - bc))
        return S


triangle = Triangle((0, 1), (1, 0), (0, 0))
print("Area of %s: %0.4f" % (triangle.name, triangle.calculate_area()))

rectangle = Rectangle((0, 0), (2, 2))
print("Area of %s: %0.4f" % (rectangle.name, rectangle.calculate_area()))

square = Square((0, 0), 2)
print("Area of %s: %0.4f" % (square.name, square.calculate_area()))

circle = Circle((0, 0), 3)
print("Area of %s: %0.4f" % (circle.name, circle.calculate_area()))

polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print("Area of %s: %0.4f" % (polygon.name, polygon.calculate_area()))
