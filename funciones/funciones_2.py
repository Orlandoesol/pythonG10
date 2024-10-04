import math
import random
import os

os.system("cls")

#ejercicio 1: funciones
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
#  IMC
""" 
def  calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)# peso / esta levada 2
    return imc

def calcular_categoria_imc(imc):
    if imc < 18.5:
        return "bajo peso"
    
    elif imc < 25:
        print(imc);
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    elif imc < 35:
        return "obesidad grado 1"
    elif imc < 40:
        return "obesidad grado 2"
    else:
        return "obesidad grado 3"
    
print(calcular_imc(85,1.70))
print(calcular_categoria_imc(calcular_imc(85,1.70))) """

#calcular el area de un circulo y el volumen de un cilindro

""" def  calcular_area_circulo(radio):
    return  math.pi * (radio ** 2)

def  calcular_volumen_cilindro(radio, altura):
    return calcular_area_circulo(radio) *  altura

radio =  float(input("ingrese el radio del circulo: "))
altura = float(input("ingrese la altura del cilindro: "))
print(f"el volumen del cilindro es {calcular_volumen_cilindro(radio, altura):.3f}") 
"""

#ejercicio 3: funciones
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
""" def media(lista):
    return sum(lista) / len(lista)

        # 0  1  2  3  4
lista =  [1, 2, 3, 4, 5]

print(f"Los elementos de la lista son: {lista}")
print(f"La suma de los elementos es: {sum(lista)}")
print(f"El tamaño de la lista es {len(lista)}")
print(f"La media de la lista es: {media(lista)}") """

#ejercicio 4: funciones
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
# 1, 4,  9, 16, 25

""" def cuadrados(lista):
    return [i ** 3 for i in lista]

lista =  [1, 2, 3, 4, 5]
print(f"Los cuadradod de los elementos de la lista son: {cuadrados(lista)}") """

#ejercicio 5: funciones
#Escribir una función que muestre los numeros que se piden por teclado, que muestre la suma de los pares y la suma de los impares.
# y cuente cuantos numeros hay en la lista; los numeros .       
""" 
def analizarNumeros():
    numeros  = [] #declaro mi lista vacia
    while True:
        entrada = input(f"Ingrese un numero (o presione \"Enter\" para terminar el programa)")
        if  entrada == "":
            break
        numeros.append(int(entrada))

    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    print(f"La lista de numeros es:  {numeros}")
    print(f"Pares: {pares}")
    print(f"Suma de pares: {sum(pares)}")
    print(f"Impares: {impares}")
    print(f"Suma de impares: {sum(impares)}")
    print(f"Cantidad de numeros: {len(numeros)}")

analizarNumeros() """

#ejercicio 6: funciones
#Escribir una funcion que use todos los metodos de la lista, usando la funcion range para generar los numeros de la lista.

def metodos_lista():


    """ lista = [random.randint(1,100) for _ in range(10)]
    return lista """
#print(metodos_lista())
    lista = [1,2,3,4,5,6,2,2,7,8,9,10]
    #random.shuffle(lista)
    print(f"lista original :  {lista}")

    #Agregar  un elemento a la lista
    lista.append(11)
    print(f"nueva lista {lista}")

    #Extender 12, 13, 14
    lista.extend([12,13,14])
    print(f"nueva lista con extend :{lista}")

    #Insert posicion + valor
    lista.insert(3, 15)
    lista.insert(0,25)
    print(f"Lista con insert: {lista}")

    #Eliminar
    lista.remove(25)
    print(f"Lista con remove: {lista}")

    #pop
    eliminado = lista.pop(8)
    print(eliminado)
    print(f"Lista con pop: {lista}")

    #count
    print(f"La lista tiene {lista.count(2)} veces el valor 2")

    #index
    print(f"El valor 3 esta en la posicion {lista.index(3)}")

    #reverse

    #lista.reverse()
    #print(f"reversa {lista}")

    #ordena el metodo sort
    lista2 = [8,2,78,123,88,3]
    lista2.sort()
    print(lista2)

    #copy
    lista3 = lista2.copy()
    print(f"copia de lista: {lista3}")

    #clear
    lista3.clear()
    print(f"lista vacia {lista3}")


metodos_lista()










