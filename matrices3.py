# Pide al usuario llenar una matriz de 2x3 y muestra su transpuesta

matriz = []

# Pedimos al usuario llenar la matriz 2x3
for i in range(2):
    fila = []
    for j in range(3):
        numero = float(input(f"Ingrese el número para la posición [{i+1},{j+1}]: "))
        fila.append(numero)
    matriz.append(fila)

# Calculamos la transpuesta de la matriz
transpuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

# Mostramos la matriz transpuesta
print("La matriz transpuesta es:")
for fila in transpuesta:
    print(fila)
