""" file = open('data1.txt', 'r',  encoding='utf-8')
data = file.read()
print(data)
file.close() """

""" with open('data1.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    #print(f"Salida dentro del with\n {data}")
 """
#print(data)

with open('data1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    lineas = data.split('\n')
    pos = file.tell()
    print(pos)

for l in data:
    print(l)



""" with open('data2.txt', 'r', encoding='utf-8') as file:
    contenido  = file.read()
    linea = contenido.split('\n')
    pos = file.tell()
    print(pos)  # imprime el contenido del archivo
 """

""" with open('data2.txt', 'r') as file:
    file.seek(7)
    pos = file.tell()
    print(pos)
    contenido = file.read()
    lineas = contenido.split('\n')
    print(lineas)  # imprime el contenido del archivo """

""" with open('data2.txt', 'r') as file:
    next = file.read(20)
    print(next)  # imprime el contenido del archivo """

""" with open('data3.txt', 'a') as archivo:
    archivo.write('Curso de python - manipulacion de archivos') """

""" with open('data1.dat', 'wb') as archivoBin:
    archivoBin.write(b'Curso de python - manipulacion de archivos\n')
    archivoBin.write(b'Grupo 10\n')
    archivoBin.write(b'Politecnico Internacional de Occidente - PIO\n')
    archivoBin.write(b'Archivo con extencion .dat')

with open('data1.dat', 'ab') as archivoBin:
    archivoBin.write(b'\nutlima linea')   
 """
#crear un archivo -w-
#leer -r-
# read, readline, readlines
""" for l in data:
    print(l.replace('\n','')) """
#agregar al fina -a-