#Calcular el imc, debe aceptar medidas inglesas, comprobar valores que sean
#numeros
#def piespulgam(pies, pulgadas = 0.0):
#    return pies * 0.3048 + pulgadas * 0.0254
#def lbsakg(lb):
#    return lb * 0.45359237
#def imc(peso, altura):
#    if altura < 1.0 or altura > 2.5 or \
#    peso < 20 or peso > 200:
#        return None 
#    return peso / altura ** 2
#print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
        return None
    return peso / altura ** 2
def InglesAmetrico(pies, libras, pulgadas = 0.0):
    convertion = []
    convertion.append(libras * 0.45359237)
    convertion.append(pies * 0.3048 + pulgadas * 0.0254)
    return convertion
def IngrDatos():
    dataSalida = []
    selection = input('Que tipo de sistema:   M ó I ---> ')
    while True:
        if selection == "M":
            dataSalida.append(float(input('Ingrese peso en kilos: ')))
            dataSalida.append(float(input('Ingrese altura en metros: ')))
            return dataSalida
        elif selection == "I":
            ingles = []
            ingles.append(float(input('Ingrese altura, pies: ')))
            ingles.append(float(input('Ingrese peso, libras: ')))
            ingles.append(float(input('Ingrese altura, pulg: ')))
            dataSalida = InglesAmetrico(ingles[0], ingles[1], ingles[2])[:]
            return dataSalida
        else:
            print('Ingrese M ó I')
            selection = input('Que tipo de sistema:   M ó I ---> ')
Manejo = IngrDatos()[:]
print(imc(Manejo[0], Manejo[1]))
