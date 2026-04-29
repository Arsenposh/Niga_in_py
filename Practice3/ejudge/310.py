class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")


s = input().split()
name = s[0]
gpa = float(s[1])

stu = Student(name, gpa)

stu.display()