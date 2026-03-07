import re

def b(text):
    str1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(b("camelCaseString"))     
print(b("PythonIsAwesome"))   
print(b("HTTPResponseCode"))   
