import math
class Point:
    def __init__(self, x = 0.00, y = 0.00):
        self.x = x
        self.y = y
    def print_info(self):
        print(f"Position: ({self.x}, {self.y})")
class Circle(Point):
    def __init__(self, x = 0.00, y = 0.00, radius = 0.00):
        super().__init__(x , y)
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius 
    def print_circle(self):
        print(f"Position: ({self.x}, {self.y}), Radius: {self.radius}, Area: {self.area():.2f}")
point = Point(3.5, 2.0)
point.print_info()

radius = Circle(4, 5, 10)
radius.print_circle()
