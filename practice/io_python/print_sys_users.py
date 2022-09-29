def main():
  usuarios = listarUsuarios()
  for usuario in usuarios:
    print(f'Usuario: {usuario}')

def listarUsuarios():
  f = open('/etc/passwd', 'r')
  datos = f.readlines()
  f.close()
  users = []
  for linea in datos:
    if linea[0] == '#' or linea[0] == '_':
      continue
    
    properties = linea.split(':')
    users.append(properties[0])
  return users

if __name__ == '__main__':
  main()