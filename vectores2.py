#Solicita 10 números y calcula el promedio de los valores ingresados.

# Inicializamos una lista vacía
numeros = []

# Pedimos al usuario que ingrese 10 números
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calculamos el promedio de los números
promedio = sum(numeros) / len(numeros)

# Mostramos el resultado
print(f"El promedio de los números ingresados es: {promedio}")


