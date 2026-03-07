import re

a = input()
b = input()
m = re.findall(re.escape(b),a)
print(len(m))
