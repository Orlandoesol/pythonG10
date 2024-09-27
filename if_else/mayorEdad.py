nombre = str(input("Nombre: "))
edad = int(input("Edad: "))
documento =  input("Documento: ").lower()


if ((edad >= 18) and (documento == "si")):
    print("Puede Entrar")
else:
    print("No Puede Entrar")

