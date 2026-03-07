import re

a = input()
m =re.findall(re.compile(r'\b\w+\b'),a)
print(len(m))
