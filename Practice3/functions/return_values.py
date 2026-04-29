# Functions can send data back to the code that called them using the return statement.

# When a function reaches a return statement, it stops executing and sends the result back:
def get_greeting():
    return "Hello from a function"

print(get_greeting())

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
    pass


def square(x):
    return x * x

num = square(6)
print(num)


def list_of_fruits():
  return ["apple", "banana", "cherry"]

fruits = list_of_fruits()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def average(nums):
    total = sum(nums)
    return total / len(nums)

print(average([10, 20, 30, 40]))


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

print(grade(87))


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(79))