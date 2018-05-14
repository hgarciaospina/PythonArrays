'''
31. Leer una matriz que guarde las notas finales de un grupo de 10 estudiantes
conformadas por 3 parciales, un trabajo y una evaluación final. Si los parciales valen
15%, el trabajo el 25%  y el final el 30%; imprimir un arreglo unidimensional que
guarde la nota definitiva de cada uno de los estudiantes.
'''

#!/usr/bin/python
import random

#Definición de variables
calificaciones = []
definitiva = []
numero_estudiantes = 10
numero_notas = 5
calificacion = 0
calculo_definitiva_estudiante = 0
n1 = 0
n2 = 0
n3 = 0
t = 0
f = 0

#Asignación de ceros a toda la matriz de 10 x 5
for i in range(numero_estudiantes):
	calificaciones.append([0]	*	numero_notas) 

#Asignación calificaciones
for i in range(numero_estudiantes):
	for j in range(numero_notas):
		calificacion = round(random.uniform(1.0, 5.0),2)
		calificaciones[i][j] = calificacion

#Cálculo definitiva por estudiantes
for i in range(numero_estudiantes):

		#Obtención nota a nota de cada alumno
		n1 = calificaciones[i][0] 
		n2 = calificaciones[i][1] 
		n3 = calificaciones[i][2]
		t = calificaciones[i][3]
		f = calificaciones[i][4]
		#Cálculo nota definitiva
		calculo_definitiva_estudiante = round((n1*0.15) + (n2*0.15) + (n3*0.15) + (t*0.25) + (f*0.30),2)
		#Se agrega la nota definitiva de cada estudiante al vector
		definitiva.append(calculo_definitiva_estudiante)

#Impresión de cada una de las notas de los estudiantes con su correspondiente nota final
print('\n')
print('----------------------------------------')
print("REPORTE DE CALIFICACIONES POR ESTUDIANTE")
print('----------------------------------------')
print('\n')

for i in range(numero_estudiantes):
	print("Estudiante ",i+1, )
	print("-------------------")
	for j in range(numero_notas):
			print("Nota: " + str(j+1) + " = " + str(calificaciones[i][j]))
			if (j == 4):
				print("Nota final:", definitiva[i])
				print('\n')				