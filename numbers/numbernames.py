""" Number Names
Show how to spell out a number in English. You can use a preexisting
implementation or roll your own, but you should support inputs up to at
least one million (or the maximum value of your language's default
bounded integer type, if that's less).

    To implement this, we split the given number n into trigrams, such
    that each trigram represents a magnitude within the given number.
    e.g.,
        152245235 turns to 235, 245, 152
    
    We place each trigram into a stack, starting with the first tigram
    (235), and then construct the pronunciations for each one until
    we have the finished pronunciation. 
"""

ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
        '5': 'five','6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
         '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
         '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
tens = {'0': '', '1': 'ten', '2': 'twenty','3': 'thirty', '4': 'forty', 
        '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', 
        '9': 'ninety'}
magnitudes = {1: '', 2: 'thousand', 3: 'million', 4: 'billion'}

# Construct the pronunciation of a trigram, given its magnitude. 
def construct_trigram(gram, magnitude):
    pronounced_gram = ""
    if len(gram) is 3:
        pronounced_gram += ones[gram[0]] + ' hundred '
        if magnitude is 1:
            pronounced_gram += teens[gram[1] + gram[2]]
        else:
            pronounced_gram += tens[gram[1]] + '-' + ones[gram[2]] + ' ' + magnitudes[magnitude] + ', '
    else:
        if magnitude is 1:
            pronounced_gram += teens[gram[1] + gram[2]]
        else:
            pronounced_gram += tens[gram[0]] + '-' + ones[gram[1]] + ' ' + magnitudes[magnitude] + ', '
    return pronounced_gram

def number_name(n):
    pronunciation = ""
    reversed_num = str(n)[::-1]
    i = 0
    stack = []
    while i < len(reversed_num):
        stack.append(reversed_num[i : i+3][::-1])
        i += 3
    current_magnitude = len(stack)
    while current_magnitude > 0:
        current_trigram = stack.pop()
        pronunciation += construct_trigram(current_trigram, current_magnitude)
        current_magnitude -= 1
    return pronunciation

print(number_name(132777523312))
