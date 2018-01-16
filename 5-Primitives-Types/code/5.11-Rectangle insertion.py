class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def isInsertion(a, b):
    return a.x <= b.x + b.width and b.x <= a.x + a.width and a.y <= b.y + b.height and b.y <= a.y + a.height


a = Rectangle(0, 0, 3, 5)
b = Rectangle(1, 1, 2, 3)
c = Rectangle(5, 6, 1, 2)
print isInsertion(a, b)
print isInsertion(a, c)
