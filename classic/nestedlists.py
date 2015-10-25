""" Nested Lists
Create a program that is able to recursively operate upon lists of
numbers, with the condition that any given list might contain more
nested lists of numbers.
"""

def recurseList(thelist):
    if len(thelist) == 1:
        return thelist.pop()
    nextitem = thelist.pop()
    if isinstance(nextitem, list):
        return recurseList(nextitem) + recurseList(thelist)
    else:
        return nextitem + recurseList(thelist)

print(recurseList([1, 2, 4, 6, [7, 4, 5]])) # 29
print(recurseList([1, 2, 4, 6, [7, 4, 5, [1, 5, 5, 5]]])) # 45
