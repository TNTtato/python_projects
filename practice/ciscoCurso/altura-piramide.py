#Determinar la altura posible de una piramide dado un numero de bloques
#disponibles. Cada capa debe ser completa, si no alcanzan los bloques
#se termina la tarea
bloques = int(input("Ingrese el número de bloques: "))

altura = 0
while altura - bloques < 0:
    altura += 1
    bloques -= altura

print("La altura de la pirámide:", altura)
