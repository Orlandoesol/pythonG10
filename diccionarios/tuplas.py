tupla = ("manzana","banano","chontaduro","mango","mango")
""" 
tupla2 = (1,2,3,4,5)
tupla3 = (True, False, False)
tupla4 = ("kiwi", 3, True)
tuplaCons = tuple(("cadena",6,False))
print(tupla) """
""" print(type(tupla))
print(len(tupla))
print(tupla2)
print(tupla3)
print(tupla4)
print(tuplaCons) """

""" #acceso a elementos
print(tupla[0])#primer elemento
print(tupla[-1])#ultimo elemento
print(tupla[1:4])
"""

""" a,b,c,d,e = ("manzana","banano","chontaduro","mango","mango")

print(f"{a} \n{b} \n{c} \n{d} \n{e}")

tupla_Concatenada =  tupla + tupla2
print(tupla_Concatenada)

nuevaT = tupla2 * 3
print(nuevaT)
print(nuevaT.count(3))
print(nuevaT.index(3))#retorna la posicion del elemento 3-1 """
""" 
deTuplaLista = list(tupla)
print(deTuplaLista) #convierte tupla a lista
print(type(deTuplaLista)) #retorna el tipo de dato de la lista
print(deTuplaLista.append("Piña"))
print(tuple(deTuplaLista))
"""

for i in range(len(tupla)):
    print(f"{i+1}.  {tupla[i]}")  #imprime cada elemento de la tupla con su respect

[print(a) for a in tupla]

