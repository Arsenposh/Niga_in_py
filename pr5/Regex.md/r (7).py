import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)

print(snake_to_camel("snake_case_example"))  
print(snake_to_camel("hello_world"))        
