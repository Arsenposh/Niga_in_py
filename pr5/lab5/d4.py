import re
a=input()
b=re.findall(r'[0-9]',a)
for i in b:
    print(i,end=" ")