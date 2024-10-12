from cryptography.fernet import Fernet
import os

os.system('cls')

key = Fernet.generate_key()
#print(f'Key:  {key.decode()}')

with open('encryp/borrador.docx', 'w') as archivo:
    archivo.write(key.decode())

filePath = 'encryp/documento.docx'

if not os.path.exists(filePath):
    print(f'El archivo {filePath} no existe\n')
else:
    print(f"El archivo  {filePath} existe\n")

def encryptFile(filePath, key):
    f = Fernet(key)
    with open('encryp/documento.docx', 'rb') as salida:
        fileData = salida.read()
    encryptedData = f.encrypt(fileData)

    with open('encryp/notificacion' + '.docx' , 'wb') as file:
        file.write(encryptedData)

encryptFile('encryp/documento.docx', key)