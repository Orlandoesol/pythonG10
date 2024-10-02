#Diferencia entre conjuntos y listas

""" conjunto = {1,2,3,34,2,1,3,5,6,7,34,34}
print(conjunto)
print(len(conjunto))
print(type(conjunto))

otroConjunto = set(("Este", "es", "un ", "conjunto", "de", "elementos"))
print(otroConjunto) """

""" if "palabra" not in otroConjunto:
    print("No esta")
else:
    print("si esta") """

""" otroConjunto.add("cadenas")

otroConjunto.update()
print(otroConjunto) """

""" otroConjunto.clear()
print(otroConjunto) """

a = {1,2,3,4,5}
b = {1,3,5,7,9}

#u = a.union(b)
#print(u) 

#u2 = a | b #union
#print(u2)
#a.update(b)

i  = a.intersection(b)
i2 = a & b #intersección

print(f"intersección  {i}") #intersección
print(f"intersección  {i2}")

d = a.difference(b)
d2 = a - b
print(f"Diferencia {d}")
print(f"Diferencia {d2}") #diferencia

ds1 =  a.symmetric_difference(b)
ds2 = a ^ b #diferencia simétrica
print(ds1)
print(ds2) #diferencia simétrica