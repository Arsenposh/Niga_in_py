class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b  

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)

nums = input().split()
a1 = int(nums[0])
b1 = int(nums[1])
a2 = int(nums[2])
b2 = int(nums[3])

p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

a_sum = p1.a + p2.a
b_sum = p1.b + p2.b
print("Result:", a_sum, b_sum)
