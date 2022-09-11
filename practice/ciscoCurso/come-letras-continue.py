#Pedir al usuario que ingrese una palabra.
#Utiliza userWord = userWord.upper() para convertir la palabra ingresada
#por el usuario a mayúsculas; hablaremos sobre los llamados métodos
#de cadena y el upper() muy pronto, no te preocupes.
#Utiliza la ejecución condicional y la instrucción continue para
#"comer" las siguientes vocales A , E , I , O , U de la palabra
#ingresada.
#Imprime las letras no consumidas en la pantalla, cada una de ellas
#en una línea separada.

userWord = input('Ingrese palabra: ').upper()

for letra in userWord:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        print(letra)
