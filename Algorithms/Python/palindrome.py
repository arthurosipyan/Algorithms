# Create a method that returns if a string is a palindrome or not.

text = "racecar"
text_1 = "basketball"


def palindrome(text_input):
    reverse = ""
    i = 0
    j = -1
    while text_input[i] == text_input[j]:
        reverse += text_input[j]
        i += 1
        j -= 1
        if reverse == text_input:
            return text_input + " is a palindrome!"
    return text_input + " is not a palindrome!"


print(palindrome(text))
