#Genera una matriz identidad de tamaño 4x4.

matriz_identidad = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

# Mostramos la matriz identidad
print("La matriz identidad de tamaño 4x4 es:")
for fila in matriz_identidad:
    print(fila)
