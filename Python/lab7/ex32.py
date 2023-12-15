import turtle
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def getArea(self):
        return ((self.radius) ** 2) * math.pi
    def getPerimeter(self):
        return 2 * self.radius * math.pi
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def draw(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.circle(self.radius)

circle = Circle(0,0,100)
circle.draw()
circle.move(10, 50)
circle.draw()

turtle.done()