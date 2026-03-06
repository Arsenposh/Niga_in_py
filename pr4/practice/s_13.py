import json
import re

NOT_FOUND = object()
def resolve_query(data, query):
    tokens = re.findall(r'[^.\[\]]+|\[\d+\]', query)
    
    current = data
    for token in tokens:
        if token.startswith('[') and token.endswith(']'):
            index = int(token[1:-1])
            if not isinstance(current, list) or index >= len(current):
                return NOT_FOUND
            current = current[index]
        else:
            if not isinstance(current, dict) or token not in current:
                return NOT_FOUND
            current = current[token]
    
    return current

data = json.loads(input())
n = int(input())
for _ in range(n):
    query = input().strip()
    result = resolve_query(data, query)
    if result is NOT_FOUND:
        print('NOT_FOUND')
    else:
        print(json.dumps(result, separators=(',', ':')))