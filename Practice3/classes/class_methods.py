class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()


class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.multiply(4, 5))  # 20


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"{self.name} is {self.age} years old"

p = Person("Bob", 25)
print(p.get_info())


class Circle:
    radius = 2
    def area(self):
        return 3.14 * self.radius**2
print(Circle().area())
