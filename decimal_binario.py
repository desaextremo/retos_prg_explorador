'''
Insignias Reto 1
Conversión número decimal a binario

validar modulo entre 2 (numero_decimal % 2)
e ir acumulando el modulo en variable

Division entre de numero_decimal // 2 e ir descompniendo numero decimal
hasta llegar a 0
'''
resultado = ""

numero_decimal = int(input())

resultado = ""
binario = ""

if numero_decimal == 0:
    resultado = "0"
    binario = ""
else:
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

    resultado = binario

print(resultado)
