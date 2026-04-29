# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

#Basic syntax
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

#Example
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
# Output: Thursday

a = 3
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is another number")
# Output: a is 3

# The underscore character _ as the last case value if you want a code block to execute when there are not other matches:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
# Output: Looking forward to the Weekend

# Combine values
# Use the | operator to combine multiple values in the same case statement:
day = 5
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("It's a weekday")
  case 6 | 7:
    print("It's a weekend")
# Output: It's a weekday

# If statements with cases
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
