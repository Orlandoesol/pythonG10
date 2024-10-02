miDiccionario = {
    #"clave":"valor"
    "nombre":"Orlando",
    "email":"docente16@pio.edu.co",
    "edad": 25,
    "peso":78,
    "persona2": {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona"
    },
    "lista": ["rojo", "azul", "verde"],
    "boleana": True
}

interno =  miDiccionario["persona2"]["ciudad"]
print(interno)
lista =  miDiccionario["lista"][1]
print(lista)
print(len(miDiccionario))



""" print(miDiccionario)
print(miDiccionario["persona2"]) """

print("************")
""" diccionario_anidado = {
    'persona1': {
        'nombre': 'Juan',
        'edad': 30,
        'ciudad': 'Madrid'
    },
    'persona2': {
        'nombre': 'Ana',
        'edad': 25,
        'ciudad': 'Barcelona'
    }
} """

#Agregar valor, clave-valor

#miDiccionario["Cargo"] = "Docente"
#print(miDiccionario)
#miDiccionario["edad"] = 46
#print(miDiccionario)
#del  miDiccionario["edad"]
#print(miDiccionario)
""" if "nombres" in  miDiccionario:
    print(f"La clave 'nombres' existe ")
else:
    print(f"La clave 'nombres' no existe ") """
""" valores =  miDiccionario.values()
print(valores) """

""" items = miDiccionario.items()
#print(items)

for clave,  valor in miDiccionario.items():
    print(f"La clave {clave} tiene el valor {valor}") """
""" 
#Cree su propio diccionario
#.get(), obtiene el valor si existe clave
edad = miDiccionario.get("edad", 0)
print(edad)
#.pop(), elimina y devuleve el valor
print(miDiccionario.pop("peso"))
#.update({clave: valor,  clave2: valor2}), agrega o actualiza valores
print(miDiccionario.update({"altura": 175, "peso": 70}))
#Ej. crear una funcion que reciba un diccionario y retorne la lista de los valores
def obtener_valores(miDiccionario):
    return list(miDiccionario.values())
print(obtener_valores(miDiccionario))
#Ej2. Una funcion que reciba un diccionario y retorne una lista de tuplas, 
# donde cada tupla contiene la clave y el valor
def obtener_tuplas(miDiccionario):
    return [(clave, valor) for clave, valor in miDiccionario.items()]
print(obtener_tuplas(miDiccionario))
 """