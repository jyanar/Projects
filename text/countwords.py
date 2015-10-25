""" Count Words in a String
Counts the number of individual words in a string. For added complexity,
read these strings in form a text file and generate a summary.
"""

def countwords(str):
    return len(str.split())

def countwords_file(filename):
    try:
        f = open(filename)
        words = f.read().split()
        f.close()
        return len(words)
    except:
        print("Error, file not found.")

print(countwords("Hello world! What a fine day!"))
print(countwords_file("word_test.txt"))
