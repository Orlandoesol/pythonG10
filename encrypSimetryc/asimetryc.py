from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

#Generar el par de claves
privateKey = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

publicKey = privateKey.public_key()

mensaje = b"Hola Grupo 10 "

mensajeEncriptado = publicKey.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),#investigar el uso y salida de los demas hashes
        label=None
    )
)

print('Mensaje Cifrado:\n',  mensajeEncriptado)
print(len(mensajeEncriptado))

mensajeDesifrado =privateKey.decrypt(
    mensajeEncriptado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),#investigar el uso y salida de los demas hashes
        label=None
    )
)

print("Mensaje Descifrado:\n", mensajeDesifrado.decode())
