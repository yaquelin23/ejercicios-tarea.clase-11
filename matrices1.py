# Solicita al usuario llenar una matriz de 3x3 y calcula la suma de todos sus elementos.

matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        numero = float(input(f"Ingrese el número para la posición [{i+1},{j+1}]: "))
        fila.append(numero)
    matriz.append(fila)

# Calculamos la suma de todos los elementos
suma_total = sum(sum(fila) for fila in matriz)

# Mostramos el resultado
print(f"La suma de todos los elementos de la matriz es: {suma_total}")
