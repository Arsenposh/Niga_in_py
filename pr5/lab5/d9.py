import re

a= input()
b = r'\b\w{3}\b'

matches = re.findall(b, a)

print(len(matches))
