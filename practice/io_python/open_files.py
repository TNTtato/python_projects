f = open('/etc/passwd', 'r')

# modo lectura 'r'
# modo append 'a'
# modo escritua 'w'
# modo create 'x'
# modo texto 't'
# modo binary 'b'

# + aumenta permisos

datos = f.read(18) # cantidad de caracteres leidos

linea = f.readline()

f.close()
print(linea)
