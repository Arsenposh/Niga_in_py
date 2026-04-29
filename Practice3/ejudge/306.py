class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

s = input().split()
leng = int(s[0])
widt = int(s[1])
rect = Rectangle(leng, widt)
print(rect.area())
