#Realiza la multiplicación de dos matrices de 2x2. Solicita los datos para ambas matrices y muestra el resultado.

matriz1 = []
matriz2 = []

# Pedimos al usuario llenar la primera matriz 2x2

print("Ingrese los valores para la primera matriz 2x2:")
for i in range(2):
    fila = []
    for j in range(2):
        numero = float(input(f"Ingrese el número para la posición [{i+1},{j+1}] de la primera matriz: "))
        fila.append(numero)
    matriz1.append(fila)

# Pedimos al usuario llenar la segunda matriz 2x2
print("Ingrese los valores para la segunda matriz 2x2:")
for i in range(2):
    fila = []
    for j in range(2):
        numero = float(input(f"Ingrese el número para la posición [{i+1},{j+1}] de la segunda matriz: "))
        fila.append(numero)
    matriz2.append(fila)

# Realizamos la multiplicación de las dos matrices
resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

# Mostramos el resultado de la multiplicación
print("El resultado de la multiplicación de las dos matrices es:")
for fila in resultado:
    print(fila)
