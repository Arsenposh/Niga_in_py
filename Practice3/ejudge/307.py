import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x-other_point.x
        dy = self.y-other_point.y
        return math.sqrt(dx*dx + dy*dy)

s = input()
x1, y1 = int(s.split()[0]), int(s.split()[1])

s = input()
x2, y2 = int(s.split()[0]), int(s.split()[1])

s = input()
x3, y3 = int(s.split()[0]), int(s.split()[1])

p1 = Point(x1, y1)
p1.show()

p1.move(x2, y2)
p1.show()
p2 = Point(x3, y3)

print(f"{p1.dist(p2):.2f}")
