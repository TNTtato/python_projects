hora = int(input("Hora de inicio (horas): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
dura += minu
minu = dura%60
hora += dura//60
hora %= 24
print('La hora de salida es ' + str(hora) + ' : ' + str(minu))
