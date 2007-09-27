# -*- coding: cp1252 -*-
# $Id$

""" 
Lee una serie de números hasta que introducimos un número negativo.

Muestra el número de entradas y la suma de los números
"""


# Pedir primero

num = input('Introduzca un número (negativo para terminar): ')
# Inicializar
suma = 0 # para acumular los números introducidos
veces = 0 # para contar los números que introduce el usuario

# Nuevas variables
mayor = num
menor = num

# Repetición
while num >= 0:
    suma = suma + num
    veces = veces + 1
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    num = input('Introduzca un número (negativo para terminar): ')    

# Salida
print 'Ha introducido', veces, 'números que suman', suma
print 'Número mayor:', mayor, 'y número menor:', menor












