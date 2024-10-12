# r:lectura w:escritura a:agregar al final b:binario
#archivo = open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_1/archivo_1.txt')
#archivo = open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_1/archivo_1.txt',  'r', encoding='utf-8')

#contenido =  archivo.read()
#contenido =  archivo.readlines()
#print(contenido)

""" with open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_1/archivo_1.txt', 'r') as archivo:
    contenido = archivo.readlines()

    #acceder a la segunda linea
    if len(contenido) >=  2:
        segundaLinea = contenido[1].strip()
        print(segundaLinea)
    else:
        print('No hay segunda linea')
"""

""" with open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_1/archivo_1.txt', 'w') as archivo:
    archivo.write('Hola mundo\n')
    archivo.write('Esto es un ejemplo de escritura en un archivo')

with open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_1/archivo_1.txt', 'a') as archivo:
    archivo.write('\nLinea final')
"""

import json

data = {
    "nombre": "Orlando",
    "edad": 25,
    "ciudad": "Armenia"
}

with open('datos.jason'  , 'w') as archivoJason:
    json.dump(data, archivoJason)  #dump: serializar datos a un archivo json

with open('datos.jason', 'r') as  archivoJason:
    datos = json.load(archivoJason)  #load: leer datos de un archivo json
    print(datos)  #imprimir datos en pantalla

with open('C:/Users/Orlando/Desktop/Ejemplo_1/Carpeta_2/json.txt', 'w') as archivo_salida:
    archivo_salida.write(str(datos))  # imprimir datos en un archivo de texto
ñ


