from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f'Circle: {self.radius=}, {self.perimeter()=}, {self.area()=}'

