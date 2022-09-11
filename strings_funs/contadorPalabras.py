import re

def countWords(words):
    numberOfWords = 0
    for word in words.split():
        x = re.findall("[A-Za-z]", word)
        if len(x):
            numberOfWords += 1
    return numberOfWords

words = input("ingresa una frase: ")
print("La frase tiene: ", countWords(words), " palabra(s)")
