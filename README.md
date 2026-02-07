# Niga_in_py
alodada

Shorthand If
If you have only one statement to execute, you can put it on the same line as the if statement.
Example
Get your own Python Server

One-line if statement:
a = 5
b = 2
if a > b: print("a is greater than b")

Logical operators are used to combine conditional statements. Python has three logical operators:

    and - Returns True if both statements are true
    or - Returns True if one of the statements is true
    not - Reverses the result, returns False if the result is true

The and Operator

The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
Example
Get your own Python Server

Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500

Nested If Statements

You can have if statements inside if statements. This is called nested if statements.
Example
Get your own Python Server
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
if a > b and c > a:
  print("Both conditions are True")

  he pass Statement

if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
Example
Get your own Python Server
a = 33
b = 200

if b > a:
  pass

The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

Why Use pass?

The pass statement is useful in several situations:

    When you're creating code structure but haven't implemented the logic yet
    When a statement is required syntactically but no action is needed
    As a placeholder for future code during development
    In empty functions or classes that you plan to implement later

pass in Development

During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.
Example

Placeholder for future implementation:
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")
pass vs Comments

A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.
Example

This will cause an error (empty code block):
score = 85

if score > 90:
  # This is excellent
# This will raise an IndentationError
Example

This works correctly with pass:
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")
pass with Multiple Conditions

You can use pass in any branch of an if-elif-else statement.
Example

Using pass in different branches:
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
