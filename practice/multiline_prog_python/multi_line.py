import _thread
import time

def horaActual(nombre_thread, tiempo_espera):
  count = 0
  while count < 5:
    time.sleep(tiempo_espera)
    count += 1
    print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ('Thread 1', 1))
_thread.start_new_thread(horaActual, ('Thread 2', 2))


while True:
  pass #se debe bloquear el programa
#de alguna manera para que se los
# hilos se ejecuten
