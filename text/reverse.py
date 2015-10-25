""" Reverse a String
Enter a string and the program will reverse it and print it out.
"""

def reverse(str):
    arr =  []
    for i in range(len(str)):
        arr.append(str[len(str) - 1 - i])
    return ''.join(arr)

print(reverse("Mississippi"))
print(reverse("Hello world!"))
