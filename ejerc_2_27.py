'''
27. Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las
matrices es igual al número mayor de la otra matriz.
'''

#!/usr/bin/python
import random

#Definición de variables
matriz_1 = []
matriz_2 = []
numero_filas = 4
numero_columnas = 5
mayor_matriz_1 = -100
mayor_matriz_2 = -100
numero_matriz_1 = []
numero_matriz_2 = []

#Asignación de ceros a las matrices de 4 x 5
for i in range(numero_filas):
	matriz_1.append([0]	*	numero_columnas) 
	matriz_2.append([0]	*	numero_columnas)

#Asignación números enteros al azar
for i in range(numero_filas):
	for j in range(numero_columnas):
		#Proceso de asignación de enteros a la matriz 1
		numero_matriz_1 = random.randrange((1000)+1)
		matriz_1[i][j] = numero_matriz_1
		#Proceso de asignación de enteros a la matriz 2
		numero_matriz_2 = random.randrange((1000)+1)
		matriz_2[i][j] = numero_matriz_2

for i in range(numero_filas):
	for j in range(numero_columnas):
		#Comparación de cada número de la matriz-1 para determinar el mayor
		if (matriz_1[i][j] > mayor_matriz_1):
			mayor_matriz_1 = matriz_1[i][j]
		
		#Comparación de cada número de la matriz-2 para determinar el mayor
		if (matriz_2[i][j] > mayor_matriz_2):	
			mayor_matriz_2 = matriz_2[i][j]	

#Determinación si los mayores de cada matriz son iguales entre si
if (mayor_matriz_1 == mayor_matriz_2):
	print("El número mayor de la matriz 1 es igual al número mayor de la matriz 2")
else:
	print("Los números mayores de cada matriz no son iguales")

print("Número mayor de la matriz 1:", mayor_matriz_1)

print("Número mayor de la matriz 2:", mayor_matriz_2)

print("\n")
print("Datos matriz 1")
print(matriz_1)
print("\n")
print("Datos matriz 2")
print(matriz_2)		
		
