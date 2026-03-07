import re

def match_a_then_b(string_to_match):
    pattern = 'ab{2,3}'

    match = re.search(pattern, string_to_match)

    if match:
        print(f"Match found in '{string_to_match}': {match.group()}")
    else:
        print(f"No match found in '{string_to_match}'.")
    
    return match

print("--- Running Examples ---")
match_a_then_b("abb")        # Matches 'abb'
match_a_then_b("abbb")       # Matches 'abbb'
match_a_then_b("cabbbd")     # Matches 'abbb'
match_a_then_b("ab")         # No match (needs at least two 'b's)
match_a_then_b("abbbb")      # Matches 'abbb' (the first part of 'abbbb')
match_a_then_b("acbd")      

result = match_a_then_b("The pattern is abbb here.")
if result:
    print(f"The matched text is: {result.group()}")
