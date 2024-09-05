# Escribe un programa que cuente cuántos números positivos se ingresan en un vector de 8 elementos.

# Inicializamos una lista vacía
numeros = []

# Pedimos al usuario que ingrese 8 números
for i in range(8):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Contamos cuántos números son positivos
contador_positivos = sum(1 for numero in numeros if numero > 0)

# Mostramos el resultado
print(f"Se ingresaron {contador_positivos} números positivos.")
