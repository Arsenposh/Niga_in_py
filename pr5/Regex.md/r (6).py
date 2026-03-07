import re

text = 'Python Exercises, PHP exercises.'
result = re.sub("[ ,.]", ":", text)

print(result) 

