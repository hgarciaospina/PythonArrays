#!/usr/bin/python
import random

'''
23. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y
determinar cuál es la fila que tiene la mayor suma.
'''

#Definición de variables
matriz = []
vector_suma_fila = []
numero_filas = 4
numero_columnas = 3
valor_elemento_matriz = 0 
suma_mayor_fila = 0
suma_elementos_fila = 0
fila = 0
columna = 0

#Asignación de ceros a las matrices de 4 x 3
for fila in range(numero_filas):
	matriz.append([0]	*	numero_columnas) 

#Asignación números enteros al azar
for fila in range(numero_filas):
	for columna in range(numero_columnas):
		#Proceso de asignación de enteros a la matriz 
		valor_elemento_matriz = random.randrange((500)+1)
		matriz[fila][columna] = valor_elemento_matriz

for fila in range(numero_filas):
	for columna in range(numero_columnas):
	  #Sumatoria de cada una de las filas
		suma_elementos_fila = suma_elementos_fila + matriz[fila][columna]
	vector_suma_fila.append(suma_elementos_fila)	
	suma_elementos_fila = 0

#Matrix con cada uno de sus elementos
print(matriz)
#Sumatoria de cada una de las filas
print(vector_suma_fila)
#Fila con la mayor suma
suma_mayor_fila = (max(vector_suma_fila))
print(suma_mayor_fila)

suma_mayor_fila = -100
for elemento_suma in range(len(vector_suma_fila)-1):
	if (vector_suma_fila[elemento_suma] > suma_mayor_fila):
		suma_mayor_fila = vector_suma_fila[elemento_suma]

print(suma_mayor_fila)