#cifrado cesr aumentado
#permitir un cambio de posicion de 1 a 25
#permitir numeros
#que mayusculas y minusculas permanezcan

message = input('Message to be encrypted: ')
def getDesplacement():
    while True:
        try:
            changePos = input('Number os positions to desplace: ')
            changePos = int(changePos)
            if(changePos >= 1 and changePos <= 25):
                return changePos
            print('ERROR: value out of range')
        except:
            print('ERROR: not valid input')
changePos = getDesplacement()
cipher = ''
for char in message:
    if char.isalnum():
        if char.isalpha():
            code = ord(char)
            if code >= ord('a') and code <= ord('z'):
                if (code + changePos) > ord('z'):
                    code = code + changePos - ord('z')
                    code = ord('a') - 1 + code
                else:
                    code += changePos
            
            if code >= ord('A') and code <= ord('Z'):
                if (code + changePos) > ord('Z'):
                    code = code + changePos - ord('Z')
                    code = ord('A') - 1 + code
                else:
                    code += changePos
            char = chr(code)
            
            cipher += char
        else:
            cipher += char
    if char == ' ':
        cipher += ' '

print(cipher)        
