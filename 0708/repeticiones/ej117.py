# -*- coding: utf-8 -*-
"""
$Id$

Haz un programa que muestre la tabla de multiplicar de un numero introducido por
teclado por el usuario. Aquí tienes un ejemplo de cómo se debe comportar el programa:

Dame un número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

# Presentación
print "*" * 50
print "Programa tabla de multiplicar"
print "*" * 50

numero = int(raw_input("Introduce un número para mostrar su tabla de multiplicar: "))

for n in range(1, 11):
    print "%d x %d = %d" % (numero, n, n*numero)

"""
SUGERENCIA:
Mejora el formato para que quede así:
5  x  1 =  5
5  x  2 = 10
5  x  3 = 15
5  x  4 = 20
5  x  5 = 25
5  x  6 = 30
5  x  7 = 35
5  x  8 = 40
5  x  9 = 45
5  x 10 = 50
"""
