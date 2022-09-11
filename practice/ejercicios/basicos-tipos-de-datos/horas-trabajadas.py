#Escribir un programa que pregunte al usuario por
#el número de horas trabajadas y el coste por hora.
#Después debe mostrar por pantalla la paga que le corresponde.
print('Horas trabajadas', '\n')
h = int(input('Ingrese el número de horas trabajadas: '))
ch = int(input('Coste por hora trabajada: '))
print('Te corresponde: ' + str(h*ch) + ' pesos')
