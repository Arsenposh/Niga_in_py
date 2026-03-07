import re

def n(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)


print(n("PythonExercises"))          
print(n("InsertSpaceBeforeCapitals"))
