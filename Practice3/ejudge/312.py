class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base
    def total_salary(self):
        return float(self.base)

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus
    def total_salary(self):
        return self.base * (1 + self.bonus / 100)

class Developer(Employee):
    def __init__(self, name, base, projects):
        super().__init__(name, base)
        self.projects = projects
    def total_salary(self):
        return self.base + 500 * self.projects

class Intern(Employee):
    pass

data = input().split()
role = data[0]
name = data[1]
base = int(data[2])

if role == "Manager":
    emp = Manager(name, base, int(data[3]))
elif role == "Developer":
    emp = Developer(name, base, int(data[3]))
else:
    emp = Intern(name, base)

print("Name:", emp.name + ",", "Total: {:.2f}".format(emp.total_salary()))
