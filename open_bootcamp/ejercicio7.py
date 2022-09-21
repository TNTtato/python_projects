from mimetypes import init


class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def __str__(self):
    strAprobado = 'Aprobado' if self.nota/10 >= 0.6 else 'Reprobado'
    return f'El alumno {self.nombre} con nota {self.nota}/10 ha {strAprobado}'

student = Alumno('Gus', 8)

print(student)