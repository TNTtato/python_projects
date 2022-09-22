import operaciones as op

def main():
  suma = op.sumar(1,2)
  resta = op.restar(3, 2)
  prod = op.multiplicar(5, 4)
  div = op.dividir(27, 3)
  
  print(f'Suma dio: {suma}\nResta dio: {resta}\nMultiplicacion dio: {prod}\nDivsion dio: {div}')

if __name__ == '__main__':
  main()