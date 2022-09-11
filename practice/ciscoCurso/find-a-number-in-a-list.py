#Encontrar e imprimir si un numero esta en una lista
myList = list(range(1, 10 + 1))
toFind = 5
elFound = False

for i in range(len(myList)):
    elFound = myList[i] == toFind
    if elFound:
        break
if elFound:
    print('Element Found in index:', i)
else:
    print('absent')
