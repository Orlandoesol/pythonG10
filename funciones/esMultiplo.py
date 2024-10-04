def es_multiplo():
    try:
        num1 =  int(input("Ingrese el primer número: "))
        num2 =  int(input("Ingrese el segundo número: "))

        if num2 == 0:
            raise ValueError("no se puede dividir por cero")
        
        if  num1 % num2 == 0:
            print(f"El número {num1} es múltiplo del numero {num2}")
        else:
            print(f"El número {num1} no es múltiplo del número {num2}")

    except ValueError as ve:
        print("ERROR!", ve)
    except Exception as ex:
        print("ERROR!, inesperado", ex)

es_multiplo()


