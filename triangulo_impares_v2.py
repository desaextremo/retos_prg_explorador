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
from funciones_captura import limpiar_pantalla

limpiar_pantalla()

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

#impresion del triangulo

cadena = ""
for fila in triangulo:
    for item in fila:
        cadena += str(item) + " "
    cadena +="\n"

print(cadena)
print("___________________________________________________")

#Imprimimos el triángulo
for fila in triangulo:

    '''
    La función map aplica una función dada a todos los elementos de una lista
    (o cualquier iterable).
    En este caso, map está aplicando la función str a cada elemento de la lista fila.
    Esto convierte cada elemento de fila a una cadena de caracteres (string).

    Por ejemplo, si fila es [5, 3, 1], map(str, fila) convertirá cada número a una cadena, resultando en ['5', '3', '1'].

    El método join toma una lista de cadenas y las concatena en una sola cadena, separándolas con el string que se especifica antes del join.
    En este caso, " ".join(...) está usando un espacio " " como separador.
    Siguiendo con el ejemplo anterior, " ".join(['5', '3', '1']) resultará en la cadena "5 3 1".
    '''
    #lista_cadenas = map(str, fila) #['7','5','3','1']
    #union = " ".join(lista_cadenas)#7 5 3 1

    #print(union)
    print(" ".join(map(str, fila)))