#Serializar datos es convertir datos
#en una cadena que pueda ser pasada
#al disco
import pickle #para serializar

class Juguete:
  nombre = ''
  precio = 0.0

  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

  def getNombre(self):
    return self.nombre

j1 = Juguete('Carro', 10.5)
f = open('datos.bin', 'wb')

pickle.dump(j1, f)
f.close()

f = open('datos.bin', 'rb')

carr = pickle.load(f)
f.close()

print(j1) #original
print(carr) #deserialized j1