#Comprobar si dos cadenas son anagramas

def areAnagrams(cadena1, cadena2):
    if(len(cadena1) == 0 or len(cadena2) == 0):
        return 'Empty String'
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    for letra2 in cadena2:
        if letra2 not in cadena1:
            return 'Not anagrams'
    return 'Angrams'

print(areAnagrams('Listen', 'Silent'))        
print(areAnagrams('modern', 'norman'))
