import re

def text_match(text):

    # The pattern '^ab*$' means:
    # ^ : Start of the string
    # a : Matches the literal character 'a'
    # b* : Matches zero or more occurrences of the literal character 'b'
    # $ : End of the string
    patterns = '^ab*$'
    if re.match(patterns, text):
        return f"'{text}' matched the pattern."
    else:
        return f"'{text}' did not match the pattern."

print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
print(text_match("abbbb"))
print(text_match("ac"))
print(text_match("ba"))
print(text_match("abbc"))

