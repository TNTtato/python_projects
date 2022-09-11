# Ingresar numeros e indicar cual es el mas grande
numeroMayor = -999999999

numero = int(input ("Introduzca un número o escriba -1 para detener:"))

while numero != -1:
    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input("Introduce un número o escribe -1 para detener:"))

print("El número más grande es:", numeroMayor)
