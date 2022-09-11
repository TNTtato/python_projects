año = int(input("Introduzca un año: "))

if año >= 1582:
    if año%4 != 0:
        BoC = "Año común"
    elif año%100 != 0:
        BoC = "Año bisiesto"
    elif año%400 != 0:
        BoC = "Año común"
    else:
        BoC = "Año bisiesto"
else:
    BoC = 'No dentro del periodo del calendario gregoriano'

print(BoC) 
