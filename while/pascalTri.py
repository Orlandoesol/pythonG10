# Pedir al usuario el número de filas
filas = int(input("Ingrese el número de filas del triángulo de Pascal: "))

# Bucle para cada fila
for i in range(filas):
    # Imprimir espacios para centrar
    for j in range(filas - i - 1):
        print(" ", end="")  # Espacio sin salto de línea

    # Calcular y mostrar los coeficientes
    coeficiente = 1  # Primer coeficiente en cada fila
    for j in range(i + 1):
        print(coeficiente, end=" ")  # Imprimir coeficiente 
        # Fórmula del coeficiente binomial
        coeficiente = coeficiente * (i - j) // (j + 1)  

    # Salto de línea después de cada fila
    print()  # Imprimir nueva línea
