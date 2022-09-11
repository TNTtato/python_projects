#función, que se comporta casi como el método original split()
def misplit(strng):
    strSplitted = []
    strSplittedReturn = []
    tempElement = ''
    for i in range(len(strng)):
        if (strng[i] == " " or strng[i] == "," and strng[i + 1] == " "):
            strSplitted.append(tempElement)
            tempElement = ''
        else:
            tempElement += strng[i]
    strSplitted.append(tempElement)
    for elem in strSplitted:
        if elem != '':
            strSplittedReturn.append(elem)
    return strSplittedReturn

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
