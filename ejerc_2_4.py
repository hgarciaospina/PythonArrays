'''

4. Almacenar 50 elementos en un vector, elevar al cuadrado cada valor almacenado en
el vector, almacenar el resultado en otro vector. Imprimir el vector original y el
vector resultante.

'''

i = 0
num = 0
original = []
cuadrados = []

while (i <= 49):
	num = num +2
	original.append(num)
	cuadrados.append(num*num)	
	i += 1
print(original)
print('\n')
print(cuadrados)
print(len(original))
	