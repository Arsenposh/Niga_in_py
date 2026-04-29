#And operator
print(True and True)   # True  
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

#Or operator
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

#Not operator
print(not True)   # False
print(not False)  # True

#Combining Boolean Operators
print((True and False) or (False or True))  # True
print(not (True and (False or True)))       # False
print((not False) and (True or False))      # True