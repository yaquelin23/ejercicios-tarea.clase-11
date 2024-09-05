# Solicita una matriz cuadrada de tamaño 3x3 y muestra los elementos de su diagonal principal

matriz = []

# Pedimos al usuario llenar la matriz 3x3
for i in range(3):
    fila = []
    for j in range(3):
        numero = float(input(f"Ingrese el número para la posición [{i+1},{j+1}]: "))
        fila.append(numero)
    matriz.append(fila)

# Mostramos los elementos de la diagonal principal
diagonal_principal = [matriz[i][i] for i in range(3)]

print(f"Los elementos de la diagonal principal son: {diagonal_principal}")
