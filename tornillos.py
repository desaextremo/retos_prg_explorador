'''
Pre-insignias Reto 1
Insignias Reto 3

Tornillos de 1 cm a menos de 3 cm (incluido): El tornillo es pequeno.
Tornillos de 3 cm a menos de 5 cm (no incluido): El tornillo es mediano.
Tornillos de 5 cm a menos de 6.5 cm (no incluido): El tornillo es grande.
Tornillos de 6.5 cm a menos de 8.5 cm (incluido): El tornillo es muy grande.
Tornillos de 8.5 cm en adelante: El tornillo es gigante.
Si el tornillo no se encuentra en ninguna de las anteriores condiciones, el sistema debe imprimir: El tamano ingresado no es valido
'''

#Caputrar el tamaño del tornillo
screw_size = float(input())

#Tornillos de 1 cm a menos de 3 cm (incluido): El tornillo es pequeno.
if 1 <= screw_size < 3:
    print("El tornillo es pequeno.")
#Tornillos de 3 cm a menos de 5 cm (no incluido): El tornillo es mediano.
elif 3 <= screw_size < 5:
    print("El tornillo es mediano.")
#Tornillos de 5 cm a menos de 6.5 cm (no incluido): El tornillo es grande.
elif 5 <= screw_size < 6.5:
    print("El tornillo es grande.")
#Tornillos de 6.5 cm a menos de 8.5 cm (incluido): El tornillo es muy grande.
elif 6.5 <= screw_size <= 8.5:
    print("El tornillo es muy grande.")
#Tornillos de 8.5 cm en adelante: El tornillo es gigante.
elif screw_size > 8.5:
    print("El tornillo es gigante.")
else:
    print("El tamano ingresado no es valido.")

'''
alternativa 2

#Tornillos de 1 cm a menos de 3 cm (incluido): El tornillo es pequeno.
if screw_size >=1 and screw_size < 3:
    print("El tornillo es pequeno.")
#Tornillos de 3 cm a menos de 5 cm (no incluido): El tornillo es mediano.
elif screw_size >=3 and screw_size < 5:
    print("El tornillo es mediano.")
#Tornillos de 5 cm a menos de 6.5 cm (no incluido): El tornillo es grande.
elif screw_size >= 5 and screw_size < 6.5:
    print("El tornillo es grande.")
#Tornillos de 6.5 cm a menos de 8.5 cm (incluido): El tornillo es muy grande.
elif screw_size >=6.5 and screw_size <= 8.5:
    print("El tornillo es muy grande.")
#Tornillos de 8.5 cm en adelante: El tornillo es gigante.
elif screw_size > 8.5:
    print("El tornillo es gigante.")
else:
    print("El tamano ingresado no es valido.")
'''