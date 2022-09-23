#Serializar datos es convertir datos
#en una cadena que pueda ser pasada
#al disco
import pickle #para serializar

class Vehiculo:
  def __init__(self, tipo, precio):
    self.tipo = tipo
    self.precio = precio

  def getTipo(self):
    return self.tipo

carro1 = Vehiculo('Carro', 100000)
f = open('./open_bootcamp/ejercicio11/datos.bin', 'wb')

pickle.dump(carro1, f)
f.close()

f = open('./open_bootcamp/ejercicio11/datos.bin', 'rb')

carro2 = pickle.load(f)
f.close()

print(carro1) #original
print(carro2) #deserialized j1