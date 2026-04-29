n = int(input())

document = {}

for i in range(n):
    line = input().split()
    command = line[0]

    if command == "set":
        key = line[1]
        value = line[2]
        document[key] = value 
    elif command == "get":
        key = line[1]
        if key in document:
            print(document[key]) 
        else:
            print(f"KE: no key {key} found in the document")
