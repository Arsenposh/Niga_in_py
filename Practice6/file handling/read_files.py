# Create a text file and write sample data
with open('sample.txt', 'w') as f:
    f.write("Hello, everyone!\n")
    f.write("I dont know what to type here\n")
    f.write("Cool python code")

# Read and print file contents
with open('sample.txt', 'r') as f:
    cont = f.read()
    print(cont)