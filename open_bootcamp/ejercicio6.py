class Vehiculo:
  def __init__(self, color, ruedas, puertas):
    self.color = color
    self.ruedas = ruedas
    self.puertas = puertas

class Coche(Vehiculo):
  def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
    super().__init__(color, ruedas, puertas)
    self.velocidad = velocidad
    self.cilindrada = cilindrada

car = Coche("negro", 4, 4, 180, 2000)

print(f'El coche es de color {car.color},', end=' ')
print(f'tiene {car.puertas} puertas,', end=' ')
print(f'es de {car.ruedas} ruedas.', end=' ')
print(f'Su velocidad max de {car.velocidad} km/h', end=' ')
print(f'y una cilindrada de {car.cilindrada} cc')