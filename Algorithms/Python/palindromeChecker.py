# Create a method that returns if a string is a palindrome or not.
text = "racecar"
text_1 = "basketball"

def palindrome(r):
    i = 0 #starting count from first char to last char
    a = len(r)-1 #starting from last char to first char (hint len() returns human length starts at 1 not 0)
    while i < len(r):
        if r[i] == r[a]: #compares the two chars
            a=a-1 #decrement back
            i=1+i #increment front
            if len(r)-1 == i: # if count which is i hits the last char return true
                return True
        else:
            return False


print(len(text_1))
if palindrome(text_1):
    print("true")
else:
    print("false")

if palindrome(text):
    print("true")
else:
    print("false")



# Create a method that returns if a string is a palindrome or not.
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



print(palindrome(text_1))

print(palindrome(text))
