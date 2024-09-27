""" 
Un programa con las operaciones basicas y complejas de aritmatica

// hay tipos de datos numericos, como int para enteros
y float para decimales
"""
#Definir las variables
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrse el siguiente número: "))

#Sumar
suma = num1 + num2
#print(suma)

#Resta 
resta = num1 - num2

#Multiplicacion
multiplicacion = num1 * num2

#Division
if  num2 != 0:
    division = num1 / num2
else:
    print("ERROR! No se puede dividir entre cero")

#Division Modular
if  num2 != 0:
    division = num1 // num2
else:
    print("ERROR! No se puede dividir entre cero")

#Potencia

potencia = num1 ** num2 # Como validar cuando la base o el exponente es cero

#Radicacion

radicacion =  num1 ** (1/num2) # Como validar cuando el indice o radicando es cero


#print("El resultado de la suma es: \'"  , suma, "\'")
print(f"El resultado de la suma es: '{suma}'")
print(f"El resultado de la resta es: '{resta}'")
print(f"El resultado de la multiplicación es: '{multiplicacion}'")
print(f"El resultado de la división es: '{division}'")#Investigar como formatear decimales
print(f"El resultado de la potencia es: '{potencia}'")#Investigar como formatear decimales
print(f"El resultado de la radicación es: '{radicacion}'")#Investigar como formatear decimales
