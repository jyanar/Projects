""" Count Vowels
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

def vowelcount(str):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in range(len(str)):
        if str[i] in vowels:
            vowels[str[i]] = vowels[str[i]] + 1
    return vowels

print(vowelcount("O what can ail thee, knight-at-arms, Alone and palely loitering?"))
