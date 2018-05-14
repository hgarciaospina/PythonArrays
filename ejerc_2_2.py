'''

2. Llenar dos vectores A y B de 15 elementos cada uno, sumar el elemento uno del
vector A con el elemento 1 del vector B y así sucesivamente hasta el elemento 15,
almacenar el resultado en un vector C e imprimir el vector resultante.

'''

A = []
B = []
C = []
suma = 0
par = 2
impar = 1

for i in range(0,15):
	A.append(par)
	B.append(impar)
	suma = A[i] + B[i]
	C.append(suma)
	par += 2
	impar += 2

for i in range(0,len(C)):
	print("Elemento - " + str(i) + " - del vector C - " + str(C[i]))