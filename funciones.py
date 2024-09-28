""" print("\"--Funcion Simple--\"")
def mensaje():    # definiendo una función
    print("Hola")    # cuerpo de la función

mensaje()    # invocación de la función

print("*******************")

print("\"--Función con argumento--\"")
def hola(nombre): #Definiendo una función
    print("Hola", nombre) # cuerpo de la función

nombre = str(input("Ingrese su nombre: "))

hola(nombre) # Invocación o llamado de la función """

print("*******************")

""" def presentar(primerNombre,segundoNombre):#orden de los parametros
    print("Hola, mi nombre es: ",primerNombre,segundoNombre)

presentar("Luke","Skywalker")
presentar("Jesse","Quick")
presentar("Clarck","Kent")

#presentar("Skywalker","Luke")# igual cantidad según los parametros
#presentar("Quick","Jesse")
#presentar("Kent","Clarck") """

print("El combinar argumentos posicionales y de palabras clave")

#Regla: primero argumentos posicionales y después los de palabras clave.

""" def suma(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

suma(1,2,3) # Invocacion pasando los parametros directamente
suma(c=1, a=2, b=3) # usando palabras claves
suma(3,c=1,b=2) #El argumento (3) para el parametro a es pasado utilizando la manera posicional.
                #Los argumentos para c y b son especificados con palabras clave. """

def resta(a,b):
    print(a-b)

resta(5,2)
resta(2,5) 
resta(a=5, b=2)
resta(a=2, b=5)
resta(5, b=2)
#resta(a=5,2)#error de sintaxis las palabras claves siempre van de segundo