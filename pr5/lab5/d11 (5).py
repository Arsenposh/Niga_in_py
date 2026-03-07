import re

a = input()

p= r'Name:\s*(.*?), Age:\s*(\d+)'

m = re.search(p, a)

if m:
    print(f"{m.group(1)} {m.group(2)}")
