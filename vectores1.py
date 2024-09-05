#Crea un programa que pida al usuario ingresar 5 números en un vector y luego calcule la suma de todos los elementos.
# Inicializamos una lista vacía
vector = []

# Pedimos al usuario que ingrese 5 números
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    vector.append(numero)

# Calculamos la suma de todos los elementos
suma = sum(vector)

# Mostramos el resultado
print(f"La suma de los elementos del vector es: {suma}")
