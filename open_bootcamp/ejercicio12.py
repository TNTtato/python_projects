paises = set(input('paises, separa con "," ').split(','))

rest = ','.join(sorted(list(paises)))
print(rest)
