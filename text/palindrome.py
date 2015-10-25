""" Check if Palindrome
Checks if the string entered by the user is a palindrome. That is that
it reads the same forwards as backwards like "racecar"
"""

def palindrome(str):
    arr =  []
    for i in range(len(str)):
        arr.append(str[len(str) - 1 - i])
    if str == ''.join(arr):
        return True
    return False

print(palindrome("racecar"))
print(palindrome("hannah"))
print(palindrome("hello world!"))
