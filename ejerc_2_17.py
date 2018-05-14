'''

17. Dado un arreglo A de N elementos se desea crear otro arreglo, tal que cada uno de
sus elementos sea la suma de los elementos opuestos en el arreglo dado.
Ejemplo Arreglo dado A= (9,5,3,10,2,8,1,7,12 )
Arreglo resultante B = (10,13,5,10)

'''

A = [9, 5, 3, 10, 2, 8, 1, 7, 12, 13, 25] 
B = []
j = 0
inicio = 0
final = len(A) - 1
ciclo = len(A) // 2
suma = 0

while j < (ciclo):
    suma = (A[inicio] + A[final])
    B.append(suma)
    inicio  +=  1 
    final -=  1
    j += 1

# Si el número de elementos del vector es impar, 
# agrega al final el valor central del vector. 
if ((len(A) % 2) == 1):
  B.append(A[ciclo])

print(B)