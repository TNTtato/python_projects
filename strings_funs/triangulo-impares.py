#Escribir un programa que pida al usuario un número
#entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
numberOfRows = int(input('Enter the heigth: '))
currentRow = []
for i in range(numberOfRows):
    currentRow.insert(0, 2 * i + 1)
    [print(i, end = " ") for i in currentRow]
    print()
