#Escribir un programa en el que se pregunte al usuario por
#una frase y una letra, y muestre por pantalla el
#número de veces que aparece la letra en la frase.
phrase = input('Enter a phrase: ')
letter = input('Enter a letter: ')
count = 0
for ch in phrase.lower():
    if ch == letter.lower():
        count += 1
print('The letter', letter, 'appears', count)
