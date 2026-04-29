# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses.

def hello(name): # name is parameter
    print(name + ", hello!")
hello("Alizhan") # Alizhan is an argument


def Sur_name(name1, name2):
    print(name1 + " " + name2)
Sur_name("Sikhimbaev", "Asankhan") #function expects 2 arguments


def My_pet(animal, name):
    print("I have a", animal)
    print("My pet is", animal, "and it\'s name is", name)
My_pet(animal = "cat", name = "Pushistik")


def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def dictionary_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

dictionary_function = {"name": "Emil", "age": 25}
my_function(dictionary_function)