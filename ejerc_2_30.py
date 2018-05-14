'''

30. Hacer un algoritmo que llene una matriz de 10 * 10 y que almacene en la diagonal
principal unos y en las demás posiciones ceros

'''

#Definición de variables
matriz = []
numero_filas = 10
numero_columnas = 10

#Asignación de ceros a toda la matriz de 10 x 10
for i in range(numero_filas):
	matriz.append([0]	*	numero_columnas) 

#Asignación de unos (1) a la diagonal principal
for i in range(numero_filas):
	for j in range(numero_columnas):
		if (i == j): #Diagonal principal
			matriz[i][j] = 1  
		 			   
for i in range(numero_filas):
	print(matriz[i])