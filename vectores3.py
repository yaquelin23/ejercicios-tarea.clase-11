#Pide al usuario ingresar 7 números y muestra cuál es el mayor de ellos.

# Inicializamos una lista vacía
numeros = []

# Pedimos al usuario que ingrese 7 números
for i in range(7):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Encontramos el número mayor
mayor = max(numeros)

# Mostramos el resultado
print(f"El número mayor es: {mayor}")
