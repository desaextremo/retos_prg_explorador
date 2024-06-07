'''
Pre-insignias Reto 3

•	La primera fila contendrá el número más pequeño 
•	Cada fila siguiente contendrá números impares en orden descendente, 
    formando un patrón de triángulo rectángulo.
•	Si el numero ingresado es par, el triángulo llegará hasta el anterior impar 
•	Entrada del Programa: El programa solicitará al usuario ingresar un número entero positivo.
•	Salida del Programa: Después de recibir la entrada del usuario, el programa mostrará en pantalla el triángulo rectángulo generado, con cada número en su posición correspondiente

Por ejemplo 
Entrada: 9
Salida: 
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
11 9 7 5 3 1

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
11 9 7 5 3 1
13 11 9 7 5 3 1
15 13 11 9 7 5 3 1

1   Solicitar al usuario que ingrese un número entero positivo.
2   Determinar el mayor número impar que es menor o igual al número ingresado (en caso de que el número ingresado sea par, se tomará el impar anterior).
3   Generar el triángulo rectángulo utilizando números impares en orden descendente para cada fila.
'''
# Solicitamos al usuario que ingrese un número entero positivo
numero = int(input())

# Si n es par, restamos 1 para obtener el número impar más cercano
if numero % 2 == 0:
    numero -= 1

# Inicializamos una lista para almacenar las filas del triángulo
triangulo = []
#7  1,3,5,7
# Generamos el triángulo
for i in range(1, numero+1, 2):
    fila = []
    for j in range(i, 0, -2):
        fila.append(j) #agrego la fila
    triangulo.append(fila)

#Imprimimos el triángulo
for fila in triangulo:
    print(" ".join(map(str, fila)))