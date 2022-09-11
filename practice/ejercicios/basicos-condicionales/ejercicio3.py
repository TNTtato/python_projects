#Los tramos impositivos para la
#declaración de la renta en un determinado país son los siguientes:

#Renta	       Tipo          impositivo
#Menos de    10000€	        5%
#Entre      10000€ y 20000€	15%
#Entre      20000€ y 35000€	20%
#Entre      35000€ y 60000€	30%
#Más de      60000€	        45%

#Escribir un programa que pregunte al usuario su renta anual y
#muestre por pantalla el tipo impositivo que le corresponde.
rent = float(input('Ingrese su renta: '))
imp = .05
if rent >= 10000 and rent < 20000:
    imp = .15
if rent >= 20000 and rent < 35000:
    imp = .20
if rent >= 35000 and rent < 60000:
    imp = .30
if rent >= 60000:
    imp = .45
print('El impuesto que le correspode es: ' + str(imp*rent))
