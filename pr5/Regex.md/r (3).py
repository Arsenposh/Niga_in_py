import re

def find_underscored_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    
    matches = re.findall(pattern, text)
    return matches

n=split(input())
results = find_underscored_sequences(n)

print(f"Найденные совпадения: {results}")
