#Escribir un programa que pregunte al
#usuario una cantidad a invertir, el
#interés anual y el número de años, y muestre por pantalla
#el capital obtenido en la inversión.

R = int(input('Monto inicial a invertir: '))
inter = int(input('Interés anual(%): '))
n = int(input('Años de inversión: '))

print('Monto por anualidad', '--------------------', '\n', sep = '\n')
Monto = R*((1 + inter/100)**n - 1)/(inter/100)
print('Su capital es: ',Monto,'\n')

print('Monto por interés comp', '-----------------------', '\n', sep = '\n')
Monto = R*(1 + inter*n/100)
print('Su capital es: ',Monto,'\n')
