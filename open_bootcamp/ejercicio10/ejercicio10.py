def main():
  #Writes all the file from the 
  #beggining
  name = './open_bootcamp/ejercicio10/test.txt'
  lineas = [
    'Hola me presento:',
    'Soy Gustavo',
    'Que tal estas?'
  ]
  fwrite(name, lineas)

  #Appends new content to an 
  # existing file
  lineas.insert(0, '\nEstoy repetido\n')
  fappend(name, lineas)

def fwrite(file, lines):
  f = open(file, 'w')
  for linea in lines:
    if not linea.endswith('\n'):
      linea += '\n'
    f.write(linea)
  f.close()

def fappend(file, lines):
  f = open(file, 'a')
  for linea in lines:
    if not linea.endswith('\n'):
      linea += '\n'
    f.write(linea)
  f.close()

if __name__ == '__main__':
  main()