print("Hola, Mundo!")
nombre = "gustavo"
##retorna una parte del string desde indice 0 a
## indice 3, el 3 no aparece
print(nombre[0:3])

##el tercer elemento entre corchete indica el salto entre
#indices
print(nombre[0:3:2])

##de principio al inidce indicado
nombre[:3]

## del indice 2 al final 
nombre[2:]

##se tiene una variable str se pude poner un .<funcion>(<valores>)
##para hacer cambios en el str, upper cambia a mayusculas todo
nombre.upper()

##input siempre retorna una cadena de caracteres
num = input("Ingrese un numero: ")
print(num)

##int(input("")) convierte el input en integer
num = int(input("Ingrese un numero: "))
print(num)

##OPERADORES
##operador + operando = expresion
##Expresion: cambinacion de elementos que resultan en valor
##al ser evaluados 
##Op aritmeticos +, -, *, /, //(div entera), **(exponente)
##%(modulo o rediduo del division)
## + con string concatena
"hola" + " " + "mundo"
##operadores logicos and, or, not(niega un valor)
false_op = (5<6) and (6>8)
true_op = (5<6) or (6>8)
#op relacionales booleanos >, <, ==, >=, <=, !=
##tambien comparan str
##operadores de asignacion
##asignan valor a variable con el valor delante del operador
## =, +=, -=, *=, /=, //=, **=, %=
##sumar uno a una variable
num1 = 1
num1 += 1
## condicional   if <condicion>: [ENTER]
##                  codigo de accion, indentacion

temp = 18
if temp < 25:
    print("Está frio")
## else solo una en un condicional
temp = int(input("Valor de temperatura: "))
if temp < 25:
    print("Esta frio")
else:
    print("Esta caliente")
##elif permite otra condicion pueden varias en un condicional
temp = int(input("Valor de temperatura: "))
if temp < 25:
    print("Esta frio")
elif (temp >= 25) or (temp < 28):
    print("Esta tibio")
else
    print("Esta caliente")

#LISTAS arrays
A123 = [1, 2 , 3, 4]
Aabc = ["a", "b", "c"]
#acceder a un elemento de un indice
A1_i0 = A123[0]
#agregar un elemento al final
#<lista>.append(<valor nuevo elemnto>)
A123.append(5)
#insertar en indice especifico sin eliminar elemento en
#ese indice
#<lista>.insert(<indice>, <elemento>)
A123.insert(1, 1.5)
