pares = 0
impares = 0
numero = int(input("Ingresa un número (negativo para terminar): "))
while numero >= 0:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = int(input("Ingresa un número (negativo para terminar): "))
print("Números pares:", pares)
print("Números impares:", impares)
