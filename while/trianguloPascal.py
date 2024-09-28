filas = int(input("Ingrese el número de filas del triángulo de Pascal: "))

# Inicializamos la primera fila
fila = [1]
print(" " * (filas - 1), 1)  # Imprimimos el 1 centrado en la primera fila

# Ciclo principal para generar las filas
i = 1
while i < filas:
    # Inicializamos la siguiente fila con 1
    nueva_fila = [1]

    # Ciclo para calcular los elementos intermedios de la nueva fila
    j = 1
    while j < i:
        # Calculamos el valor del elemento sumando los dos elementos anteriores
        valor = fila[j-1] + fila[j]
        nueva_fila.append(valor)
        j += 1

    # Agregamos el último 1 a la nueva fila
    nueva_fila.append(1)

    # Calculamos los espacios necesarios para centrar la fila
    espacios = filas - i - 1

    # Imprimimos los espacios iniciales
    print(" " * espacios, end="")

    # Imprimimos la fila
    for num in nueva_fila:
        print(num, end=" ")

    # Salto de línea al final de la fila
    print()

    # Actualizamos la fila actual
    fila = nueva_fila

    i += 1