#Si el ingreso del ciudadano no era superior a 85,528 pesos,
#el impuesto era igual al 18% del ingreso
#menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
#Si el ingreso era superior a esta cantidad, el impuesto era igual
#a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
#Debe aceptar un valor de punto flotante: el ingreso.
#A continuación, debe imprimir el impuesto calculado,
#redondeado a pesos totales. Hay una función llamada round() que hará el
#redondeo por ti, la encontrarás en el código de esqueleto del editor.

ingreso=float(input("Ingrese el ingreso anual: "))

impuesto = ingreso*.18 - 556.2
if impuesto > 0:
    if ingreso > 85528:
        impuesto = 14839.2 + (ingreso - 85528)*.32
else:
    impuesto = 0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
