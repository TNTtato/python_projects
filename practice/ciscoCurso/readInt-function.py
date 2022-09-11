#función capaz de ingresar valores enteros y verificar si están
#dentro de un rango especificado

def readInt(prompt, minVal, maxVal):
    while True:
        try:
            numberRange = int(input(prompt))
            if numberRange >= minVal and numberRange <= maxVal:
                return numberRange
            else:
                print('Error: No está dentro del rango', '(' + str(minVal) + ' ... ' + str(maxVal) + ')')
        except ValueError:
            print('Error: entrada incorrecta')
        except:
            print('Unknown')

v = readInt("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
