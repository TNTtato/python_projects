#Intercambiar lugares de una lista sin importar el tamaño
#si la lista tiene logintud impar el elemento del medio queda en el mismo lugar
N = 5
myList = list(range(1, N + 1)) #list from 1 to N
lenght = len(myList)
for i in range(lenght//2):
    myList[i], myList[lenght - i -1] = myList[lenght - i -1], myList[i]
print(myList)
