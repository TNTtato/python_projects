from functools import reduce
from random import sample

n = 10
lista = sample(range(1, 100+1), n)

impares = list(filter(lambda x: x % 2, lista))
suma = reduce(lambda a, b: a + b, impares)

print(lista, impares, suma, sep=' ---> ')
