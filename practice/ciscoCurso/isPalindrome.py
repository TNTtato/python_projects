#programa que dice si es palindromo un texto ingresado

def isPalindrome(cadena):
    if len(cadena) == 0:
        return 'Not a palindrome'
    cadena = cadena.lower()
    cadTemp = ''
    for letter in cadena:
        if letter.isalpha():
            cadTemp += letter
    cadena = cadTemp
    if cadena == cadena[::-1]:
        return 'Is a palindrome'
    return 'Not a palindrome'

print(isPalindrome('Ten animals I slam in a net'))
print(isPalindrome('Eleven animals I slam in a net'))
print(isPalindrome(''))
