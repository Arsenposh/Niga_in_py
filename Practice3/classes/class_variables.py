class City:
    population = 100000
c = City()
print(c.population)


class Laptop:
    brand = "Lenovo"
l = Laptop()
print(l.brand)


class Team:
    country = "Kazakhstan"
player = Team()
print(player.country)


class Car:
    wheels = 4
c1 = Car()
c2 = Car()
Car.wheels = 6
print(c1.wheels, c2.wheels)


class Cat:
    color = "Black"
c1 = Cat()
c1.color = "White"
c2 = Cat()
print(c1.color)
print(c2.color) 
