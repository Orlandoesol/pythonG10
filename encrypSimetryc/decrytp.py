from cryptography.fernet import Fernet
import os

os.system('cls')

with open('encryp/borrador.docx', 'r') as llave:
    key = llave.read()

    fileDataDecrypt = "encryp/notificacion.docx"

if not os.path.exists(fileDataDecrypt):
    print(f'El archivo {fileDataDecrypt} no existe\n')
else:
    print(f"El archivo  {fileDataDecrypt} existe\n")

def decrypFile(fileDataDecrypt, key):
    f = Fernet(key)
    with open('encryp/notificacion.docx', 'rb') as file:
        encrypData =  file.read()
    decryptedData = f.decrypt(encrypData)
    with open('encryp/mensaje.docx', 'wb') as fileMen:
        fileMen.write(decryptedData)

decrypFile('encryp/notificacion.docx', key)
