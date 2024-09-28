import math

def calcularAreaPerimetro():
    try:
        radio = float(input("Ingrese el radio: "))

        if radio < 0:
            raise ValueError("El radio no puede ser negativo")
        
        #area =  math.pi * (pow(radio))
        area2 = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio

        #print(f"Area del circulo es: {area:.2f}")
        print(f"Area 2 del circulo es: {area2:.2f}")
        print(f"Perimetro del circulo es: {perimetro:.3f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error, inesperado: {e}")

calcularAreaPerimetro()

