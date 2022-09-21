class Vehiculo:
  color = 'negro'
  ruedas = 4
  puertas = 4

class Coche(Vehiculo):
  velocidad = 80
  cilindrada = 1000

car = Coche()

print(car)