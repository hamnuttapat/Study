import turtle as t

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)

    def intersect(self, other):
        x_overlap = max(0, min(self.x + self.width, other.x + other.width) - max(self.x, other.x))
        y_overlap = max(0, min(self.y + self.height, other.y + other.height) - max(self.y, other.y))
        
        if x_overlap > 0 and y_overlap > 0:
            overlap_width = x_overlap
            overlap_height = y_overlap
            
            overlap_size = min(overlap_width, overlap_height)
            overlap_x = max(self.x, other.x)
            overlap_y = min(self.y, other.y)
            
            return Rectangle(overlap_x, overlap_y, overlap_size, overlap_size)
        else:
            return None

A = Rectangle(0, 0, 100, 200)
B = Rectangle(-50, 50, 100, 100)

t.speed(10)  


A.draw()
B.draw()


C = A.intersect(B)
if C:
    t.pencolor("red")
    C.draw()

t.done()
