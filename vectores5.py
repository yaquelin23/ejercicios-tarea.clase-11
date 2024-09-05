# Crea un programa que invierta el orden de un vector de 6 elementos.

# Inicializamos una lista vacía
numeros = []

# Pedimos al usuario que ingrese 6 números
for i in range(6):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Invertimos el orden de los números
numeros_invertidos = numeros[::-1]

# Mostramos el vector invertido
print(f"El vector invertido es: {numeros_invertidos}")
