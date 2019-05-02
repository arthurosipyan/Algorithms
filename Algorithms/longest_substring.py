# Find longest substring of non-repetitive characters.

text_input = "aaasdasdc"


def longest_substring(text):
    response = ""
    i = 0
    while i < len(text)-1:
        if text[i] != text[i+1]:
            response+= text[i]
        i =i+ 1
    return response


print(longest_substring(text_input))
