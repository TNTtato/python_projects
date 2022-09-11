#quitar elementos repetidos de una lista
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tempList = []
for i in range(len(myList)):
    if myList[i] not in tempList:
        tempList.append(myList[i])
myList = tempList[:]

print("List with unique values: ")
print(myList)
