# Append new lines and verify content
with open('sample.txt', 'a') as f:
    f.write("\nIt is really cool code")
    f.write("\nNew text line")