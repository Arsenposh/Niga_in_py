import re

a = input()
p = re.compile(r'^\d+$')

if p.match(a):
    print("Match")
else:
    print("No match")
