import re

a= input()

b=re.findall(r'[A-Z]', a)
print(len(b))

