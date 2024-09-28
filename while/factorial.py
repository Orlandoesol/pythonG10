numero = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print("El factorial de", numero, "es:", factorial)

#1 * 2 * 3 * 4