'''

18. Dado un arreglo A de N elementos se desea generar tres arreglos que contenga los
elementos negativos, cero y positivos del arreglo.

'''

from random import randint

numero = randint(0, 500)

i = 0
j = 0
ivn = 0
ivc = 0
ivp = 0
A = []
NE = []
CE = []
PO = []

N = int(input("Ingrese el número de elementos del arreglo que desea : "))

#Se ingresan los elementos del vector A 
while (i < N):
	numero = int(input("Ingrese el elemento: "))
	A.append(numero)
	i += 1
	
#Búsqueda secuencial en el vector de los números negativos, ceros y positivos
#y se agregan a sus respectivos vectores
while (j < N):
	elemento = A[j]
	if (A[j] < 0):
		NE.append(elemento)
	elif (A[j] == 0):
		CE.append(elemento)
	else:
		PO.append(elemento)
	j += 1	

#Impresión de resultados
print(A)
print(NE)
print(CE)
print(PO)