'''

3. Llenar un vector de 20 elementos, imprimir la posición y el valor del elemento mayor
almacenado en el vector. Suponga que todos los elementos del vector son
diferentes.

'''

from random import randint

i = 0
j = 1
posicion = 0
vector = []
numero = randint(0, 500)
vector.append(numero)
longitud = 0

# Se generan los 20 números aletoramienta y se busca el número generado 
# en el vector. Si se encuentra en el vector se genera un nuevo número
# de lo contraroo se agrega a la lista

while (i < 19):
	numero = randint(0, 500)
	if  (numero in vector):
			numero = randint(0, 500)
	else:
			i += 1
			vector.append(numero)
longitud = len(vector)
	
#Búsqueda secuencial en el vector sin ordenar del número mayor
#Hacemos a la variable mayor igual a la primera posición del vector

mayor = vector[0]
while (j <= 19) :
	if (vector[j] > mayor):
		mayor = vector[j]
		posicion = j
	j += 1	

print("El número mayor del vector es: ", vector[posicion])
print("Y se encuentra en la posicion", posicion)


# Ordena el vector de menor mayor, luego el mayor es el número
# de la última posición que es la 19

vector.sort()			
print(vector)

print("El número mayor es " + str(vector[longitud-1]) + " y se encuentra en la posicíon " + str(longitud-1))