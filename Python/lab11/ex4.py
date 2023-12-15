import turtle as t
from abc import ABC, abstractmethod

class TwoDShape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__((x1 + x2) / 2, (y1 + y2) / 2) 
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        t.penup()
        t.goto(self.x1, self.y1)
        t.pendown()
        t.goto(self.x2, self.y2)

class Rectangle(TwoDShape):
    def __init__(self, x, y, width, height):
        super().__init__(x + width / 2, y - height / 2) 
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)

class Circle(TwoDShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        t.penup()
        t.goto(self.x, self.y - self.radius)
        t.pendown()
        t.circle(self.radius)


line = Line(0, 0, 100, 100)
rectangle = Rectangle(50, 50, 80, 60)
circle = Circle(-50, -50, 30)

line.draw()
rectangle.draw()
circle.draw()

t.done()