import os

os.system("cls")

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = (1,2,3)

""" print(tupla1 and tupla2)
print(tupla1 or  tupla2)
print(not tupla1) """
#print(tupla1 == tupla2)
#print(tupla1 !=  tupla3)
#print(tupla1 > tupla3) #<, >,<=,>=
print(tupla1)
print(9 in tupla1)
print(1 in tupla1)
print(1 not in tupla1)
print(4 not in tupla1)

valor = 3
print(all(x >= valor for x  in tupla1))
print(any(x >= valor for x  in tupla1))
print(max(tupla1))
print(min(tupla1))

mi_tupla = (1,2,3,5>2,7!=7,9,0 )
print(mi_tupla)





