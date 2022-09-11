numeroEntrada = input('Ingrese un numero entero a convertir a binario: ')
numeroEntero = int(numeroEntrada)
binary = []
while numeroEntero // 2 != 0:
    binary.append(numeroEntero % 2)
    numeroEntero //= 2
binary.append(1)
binary = binary[::-1]
print(binary)
    
