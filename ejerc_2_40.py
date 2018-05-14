'''
40. El dueño de una cadena de almacenes de artículos deportivos desea controlar sus
ventas por medio de una computadora. Los datos de entrada son:
	a) El número del almacén (1 a 50)
	b) Un número que indica el deporte del artículo (1 a 20)
Hacer un programa que escriba al final del día lo siguiente:
	1. Las ventas totales en el día para cada almacén.
	2. Las ventas totales para cada uno de los deportes.
	3. Las ventas totales de todos los almacenes
'''

#!/usr/bin/python
import random

#Definición de variables
#cadena_almacenes[i][j]- para i=0..49 - para j=0..19 
# i = número almacen, j = numero artículo
cadena_almacenes = []
ventas_totales_diarias_x_almacen = []
ventas_totales_x_deporte = []
numero_de_almacenes = 50
numero_deporte_articulo = 20
numero_almacen = 0
numero_articulo = 0
venta_articulo_almacen = 0
ventas_articulos_deportes = 0
total_general_almacenes = 0
total_general_deportes = 0

#Asignación de ceros a toda la matriz de 50 x 20
for i in range(numero_de_almacenes):
	cadena_almacenes.append([0]	*	numero_deporte_articulo)

#Asignación de ceros ventas totales diarias por almacen
for i in range(numero_de_almacenes):
	ventas_totales_diarias_x_almacen.append(0)

#Asignación de ceros ventas totales diarias por deporte
for i in range(numero_deporte_articulo):
	ventas_totales_x_deporte.append(0)	


#Asignación ventas por artículo en cada almacen
for numero_almacen in range(numero_de_almacenes):
	for numero_articulo in range(numero_deporte_articulo):
		venta_articulo_almacen = random.randint(1, 10)		
		cadena_almacenes[numero_almacen][numero_articulo] = venta_articulo_almacen
		print("almacen",numero_almacen,"numero artículo", numero_articulo, "venta:", cadena_almacenes[numero_almacen][numero_articulo])

#Proceso de ventas totales diarias por almacen
for numero_almacen in range(numero_de_almacenes):
	for numero_articulo in range(numero_deporte_articulo):
		ventas_totales_diarias_x_almacen[numero_almacen] = ventas_totales_diarias_x_almacen[numero_almacen] + cadena_almacenes[numero_almacen][numero_articulo] 
	total_general_almacenes = total_general_almacenes + 	ventas_totales_diarias_x_almacen[numero_almacen]	

for numero_almacen in range(numero_de_almacenes):
	for numero_articulo in range(numero_deporte_articulo):
		print("Almacen : ",numero_almacen, "articulo", numero_articulo, "venta articulo", cadena_almacenes[numero_almacen][numero_articulo])	
	print("\n")
	print("--------------------------------------------------------")	

for numero_almacen in range(numero_de_almacenes):
	print("Almacen : ",numero_almacen, "venta total diaria almacen", ventas_totales_diarias_x_almacen[numero_almacen])	
	print('\n')

print("Total venta general de los 50 almacenes ", total_general_almacenes)

#Proceso de ventas totales por deporte
for numero_articulo in range(numero_deporte_articulo):
	for numero_almacen in range(numero_de_almacenes):
		ventas_totales_x_deporte[numero_articulo] = ventas_totales_x_deporte[numero_articulo]  + cadena_almacenes[numero_almacen][numero_articulo]
	total_general_deportes = total_general_deportes + ventas_totales_x_deporte[numero_articulo]

for numero_articulo in range(numero_deporte_articulo):
	print("Deporte : ",numero_articulo, "venta total por deporte", ventas_totales_x_deporte[numero_articulo])	
	print('\n')

print("Total venta general de los 20 deportes x cada uno de los 50 almacenes ", total_general_almacenes)