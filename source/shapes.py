

import math


class Shape:

    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, readius):
        self.radius = readius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    