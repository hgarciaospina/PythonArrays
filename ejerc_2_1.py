'''

1. Calcular el promedio de 10 valores almacenados en un vector. Determinar además
cuantos son mayores que el promedio, imprimir el promedio, el número de datos
mayores que el promedio y un listado de los valores que resultaron ser mayores al
promedio.

'''

vector = [25, 100, 30, 95, 80, 45, 87, 63, 11, 29]
mayores_promedio = []
promedio  = 0
suma = 0
cuenta_mayores_promedio = 0
i = 0
j = 0

for i in range(0,10):
	suma = suma + vector[i]

promedio = suma / 10


for i in range(0,10):
	if (vector[i] > promedio):
		mayores_promedio.append(vector[i])
		j	+=	1

cuenta_mayores_promedio = len(mayores_promedio)

print("El promedio de los 10 números es: " + str(promedio))
print("Hay " + str(cuenta_mayores_promedio) + " números mayores al promedio")

for i in range(0, cuenta_mayores_promedio):
	print("Número mayor al promedio: " + str(mayores_promedio[i]))