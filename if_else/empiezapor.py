# Python
palabra = input("Ingrese una palabra: ")
letra_inicial = input("Ingrese la letra inicial a buscar: ")

if palabra[0].lower() == letra_inicial.lower():
    print("La palabra empieza con", letra_inicial)
else:
    print("La palabra no empieza con", letra_inicial)