'''
Pre- Insignias Reto 2
Insignias Reto 2

Condiciones de Apilado Triangular: Dado un número natural n, 
se puede apilar de manera triangular si existe un nivel tal que
la suma total de latas hasta ese nivel sea igual a n.

triangular= nivel * (nivel+1)/2

1,3,6,10 lata (SI)

Cantidad de latas:3,4,5,6...
	
nivel 1 	  1       =  triangular en nivel 1: 1 * (1 + 1)//2 =  1
nivel 2      1 1      =  triangular en nivel 2: 2 * (2 + 1)//2 =  3
nivel 3     1 1 1     =  triangular en nivel 3: 3 * (3 + 1)//2 =  6
nivel 4    1 1 1 1       =  triangular en nivel 4: 4 * (4 + 1)//2 =  10
nivel 5   1 1 1 1 1   =  triangular en nivel 5: 5 * (5 + 1)//2 =  15
nivel 6  1 1 1 1 1 1  =  triangular en nivel 6: 6 * (6 + 1)//2 =  21

'''

numero_latas = int(input())
triangular = 0
nivel = 0

while triangular < numero_latas:
    nivel +=1
    triangular = (nivel * (nivel + 1)) // 2

if triangular == numero_latas:
    print(f"{numero_latas} es adecuado para apilar.")
else:
    print(f"{numero_latas} no es adecuado para apilar.")