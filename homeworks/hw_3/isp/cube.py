from shape import Shape
from shape3d import Shape3d


class Cube(Shape, Shape3d):
    def __init__(self, edge: float):
        self.edge = edge

    def area(self):
        return 6 * self.edge ** 2

    def perimeter(self):
        return 12 * self.edge

    def volume(self):
        return self.edge ** 3

    def __str__(self):
        return f'Cube: {self.edge=}, {self.perimeter()=}, {self.area()=}, {self.volume()=}'

