text = "racecar"
text_1 = "basketball"


def palindrome(text_input):
    i = 0
    j = -1
    while text_input[i] == text_input[j]:
        i += 1
        j -= 1
        if i == len(text_input)-1:
            return text_input + " is a palindrome!"

    return text_input + " is not a palindrome!"


print(palindrome(text))
print(palindrome(text_1))
