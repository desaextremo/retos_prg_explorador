'''
Pre- Insignias Reto 2
Insignias Reto 2

Condiciones de Apilado Triangular: Dado un número natural n, 
se puede apilar de manera triangular si existe un nivel tal que
la suma total de latas hasta ese nivel sea igual a n.

triangular=va llevando la suma de latas en cada nivel

1,3,6,10 lata (SI)

Cantidad de latas:3,4,5,6...
	
nivel 1 	    1       =  triangular 1
nivel 2        1 1      =  triangular 3
nivel 3       1 1 1     =  triangular 6 
nivel 4      1 1 1 1    =  triangular 10
nivel 5     1 1 1 1 1   =  triangular 15
nivel 6   1 1 1 1 1 1 1 =  triangular 21
En esta versión realizamos la validación simplemente sumando la cantidad de latas
en cada nivel y esta cuenta la lleva la variable 'triangular'

Sumaremos la cAntidad de latas en el nivel, hasta que 'triangular' sea mayor o igual a n
'''

numero_latas = int(input())

triangular = 0
nivel = 0

while triangular < numero_latas:
    nivel += 1
    triangular += nivel

if triangular == numero_latas:
    print(f"{numero_latas} es adecuado para apilar.")
else:
    print(f"{numero_latas} no es adecuado para apilar.")
