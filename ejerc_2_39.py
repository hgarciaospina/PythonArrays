'''
39. En la U.L.A. (Universidad de Los Andes) se conoce el número de alumnos que
ingresaron en sus 4 diferentes carreras de Ingeniería (Ingeniería Civil, Mecánica,
Eléctrica y Sistemas), en los últimos 5 años. Construya un programa que proporcione
la siguiente información:
a. Total de alumnos por año.
b. Porcentaje de alumnos ingresados en el año X de la carrera Y.
c. ¿En qué año y en qué carrera se dio el menor ingreso de alumnos?
d. Año en el cual la carrera Y tuvo el mayor ingreso de alumnos
'''

#!/usr/bin/python
from random import randint

#Definición de variables
anios = 5
carreras = 4
total_alumnos_anio = 0
porcentaje_alumnos_ingresados_anio_x_carrera_y = 0
menor_ingreso_alumnos_anio = 100000
menor_ingreso_alumnos_carrera = 100000
anio_carrera_y_mayor_ingreso_alumnos = 0
alumnos_anio_carrera = []
anio_carrera = 0

#Asignación de ceros a toda la matriz de 5 x 4
for i in range(anios):
	alumnos_anio_carrera.append([0]	*	carreras) 

#Asignación de estudiantes por año en cada carrera
for i in range(anios):
	for j in range(carreras):
		anio_carrera = randint(15, 30)
		alumnos_anio_carrera[i][j] = anio_carrera

print(alumnos_anio_carrera)

