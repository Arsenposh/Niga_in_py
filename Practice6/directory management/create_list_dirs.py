# Create nested directories
import os
os.makedirs('python/codes/examples')

# List files and folders
files = os.listdir(".")
print(files)

# Find files by extension
for f in files:
    if f.endswith('.txt'):
        print(f)
