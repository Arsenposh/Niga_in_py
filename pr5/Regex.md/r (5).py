import re

def match_a_to_b(text):
    pattern = 'a.*b'
    if re.search(pattern, text):
        return True, re.search(pattern, text).group(0)
    else:
        return False, None
test_strings = [
    "I have a big red apple.",
    "This is a test string, maybe it has a match here, for example 'a...b'",
    "The rain in Spain stays mainly in the plain.",
    "aardvark",
    "book"
]

for s in test_strings:
    is_match, matched_substring = match_a_to_b(s)
    if is_match:
        print(f"'{s}' -> MATCH FOUND. Substring: '{matched_substring}'")
    else:
        print(f"'{s}' -> NO MATCH.")
