#Para tributar un determinado impuesto se debe
#ser mayor de 16 años y tener unos ingresos iguales
#o superiores a 1000 € mensuales. Escribir un programa
#que pregunte al usuario su edad y sus ingresos mensuales y
#muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input('Escribe la edad: '))
ingr = int(input('Ingresos: '))
tribu = "NO"
if edad > 16 and ingr >= 1000:
    tribu = "SI"
print(tribu + ' debes tributar')
