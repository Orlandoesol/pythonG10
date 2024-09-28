import random
numero_secreto = random.randint(1, 20)
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número (1-20): "))
    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print("¡Correcto!")
        adivinado = True
