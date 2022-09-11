#Given three lenghts, tell if is possible to make a triangle out of this
#values and print if is also rectangle and returns the area, if it´s possible
#to make one
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b
def esUnTrianguloRectangulo(a, b, c):
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
def HeronFormula(a, b, c):
    s = (a + b + c) / 2
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return A
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
    print("Es rectangulo? ----->  ", esUnTrianguloRectangulo(a, b, c))
    print("El area de este triangulo es:   ", HeronFormula(a, b, c))
else:
    print("Lo siento, no puede ser un triángulo.")
