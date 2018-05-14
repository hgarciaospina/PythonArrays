'''

32. Hacer un algoritmo que llene una matriz de 5 * 6 y que imprima cuantos de los
números almacenados son ceros, cuántos son positivos y cuantos son negativos.

'''
from random import randint

#Definición de variables
matriz = []
numero_filas = 5
numero_columnas = 6
numero = 0
negativos = 0
ceros = 0
positivos = 0
i = 0
j = 0

for i in range(numero_filas):
	matriz.append([0] * numero_columnas)
			
for i in range(numero_filas):
	for j in range(numero_columnas):
		numero = randint(-15, 15)
		matriz[i][j] = numero
		 			   
for i in range(numero_filas):
	print(matriz[i])

for i in range(numero_filas):
	for j in range(numero_columnas):
		if (matriz[i][j] < 0):
			negativos	+=	1
		elif(matriz[i][j] > 0):
			positivos +=1 
		else:
			ceros +=1

print("La matriz tiene " + str(negativos) + " números negativos")		
print("La matriz tiene " + str(positivos) + " números positivos")		
print("La matriz tiene " + str(ceros) + " números ceros")	
			

