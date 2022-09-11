#programa que puede simular el funcionamiento de un display de siete segmentos
#se debe mostrar por consola una representacion del numero ingresado
#si ingresa 123, mostrar
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ###

#def sevenSegments(number):
def genNumbersMatrix():
    zero = ['#'*3, '# #', '# #', '# #', '#'*3]
    one = ['  #' for i in range(5)]
    two = ['#'*3, '  #', '#'*3, '#  ', '#'*3]
    three = ['#'*3, '  #', '#'*3, '  #', '#'*3]
    four = ['# #', '# #', '#'*3, '  #', '  #']
    five = ['#'*3, '#  ', '#'*3, '  #', '#'*3]
    six = ['#'*3, '#  ', '#'*3, '# #', '#'*3]
    seven = one[1:]
    seven.insert(0, '#'*3)
    eigth = ['#'*3, '# #', '#'*3, '# #', '#'*3]
    nine = ['#'*3, '# #', '#'*3, '  #', '  #']

    zeroToNine = [zero, one, two, three, four, five, six, seven, eigth, nine]
    while True:
        numero = input(('Ingrese numero, entero y positivo: '))
        try:
            if int(numero) < 0:
                print('ERROR: Entrada negativa')
            else:
                numbersToDisplay = []
                for num in numero:
                    numbersToDisplay.append(zeroToNine[int(num)])
                return numbersToDisplay
        except ValueError:
            print('ERROR: Entrada errada,', numero, 'no es un numero')
        except:
            print('ERROR: Entrada no esperada')
            
numbersToDisplay = genNumbersMatrix()
for l in range(5):
    for m in range(len(numbersToDisplay)):
        print(numbersToDisplay[m][l], end = ' ')
    print()

