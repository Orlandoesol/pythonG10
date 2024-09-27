while True:

    palabra = "Colombia"
    letraInicial = input("Ingrese la letra inicial: ")

    if palabra[0].lower() ==  letraInicial.lower():
        print(f"La palabra {palabra} comienza con la letra {letraInicial} ingresada")
    else:    
        print(f"La palabra {palabra} no comienza con la letra {letraInicial} ingresada")