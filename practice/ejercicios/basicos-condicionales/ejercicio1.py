#Escribir un programa que pida al usuario un número
#entero y muestre por pantalla si es par o impar.

num = int(input('Ingrese un entero: '))
cond = "Impar"
if num % 2 == 0:
    cond = "Par"
print('El numero: ' + str(num) + " es " + cond)
