'''

16. Codifique un programa tal, que dado como entrada un arreglo unidimensional de
enteros y un número entero, determine cuántas veces se encuentra este número
dentro del arreglo.

'''

i = 0
contador = 0


numeros = [1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 
					 7, 7, 7, 7, 7, 12, 13, 14, 16, 20, 34, 34, 34, 
					 68, 68, 68, 68
					]

numero = 68

print(numeros)

while i < (len(numeros)):
	if (numeros[i] == numero):
		contador += 1
	i += 1	

print(contador)	