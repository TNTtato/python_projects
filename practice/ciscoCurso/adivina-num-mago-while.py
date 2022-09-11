numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numIng = int(input('Ingresa un numero entero: '))
while numIng != numeroSecreto:
    print('¡Ja, ja! ¡Estás atrapado en mi ciclo!')
    numIng = int(input('Ingresa un numero entero: '))
print('¡Bien hecho, muggle! Eres libre ahora')
