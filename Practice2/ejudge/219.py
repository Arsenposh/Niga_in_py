n = int(input())
dictio = {}

for i in range(n):
    line = input().split()
    name = line[0]
    count = int(line[1])
    
    if name in dictio:
        dictio[name] += count
    else:
        dictio[name] = count  

for name in sorted(dictio.keys()):
    print(name, dictio[name])