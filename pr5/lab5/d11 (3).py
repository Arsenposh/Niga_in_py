import re

a = input()
m = re.findall(r'\w+', a)

print(len(m))
