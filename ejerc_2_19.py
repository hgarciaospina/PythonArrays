'''

19. Dado un arreglo A de N elementos se quiere generar otro arreglo que 
contenga las posiciones de los elementos del arreglo dado que sean iguales
a un valor x dado.
Ejemplo : Arreglo dado A = (4,6,8,2,6,9,6,1)
X=6
Arreglo resultante B = (2,5,7)

'''

from random import randint

i = 0
j = 0
x = 0
N = 0
posicion = 0
numero = 0
A = []
B = []

N = int(input("Ingrese el número de elementos que desea almacena en el arreglo: "))

while (i < N):
	numero = int(input("Ingrese un número :"))
	A.append(numero)
	i += 1

x = int(input("Ingrese el número a verificar: "))

while (j < len(A)):
	if  (x == A[j]):
			posicion = j
			B.append(posicion)
	j += 1

print(B)