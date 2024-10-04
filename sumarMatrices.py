import numpy as np

#Algoritmo para sumar matrices en python

matrizA =  np.array([[1, 2, 3], [4, 5, 6],[7, 8,  9]])
matrizB =  np.array([[10, 11, 12], [13,  14, 15],[16, 17, 18]])

matrizC = matrizA + matrizB
matrizD = matrizC ** 2
print(matrizA)
print("*********************")
print(matrizB)
print("***Resultado de la suma***")
print(matrizC)
print("***Resultado de cuadrados***")
print(matrizD)

