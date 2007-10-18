# -*- coding: utf-8 -*-
"""
$Id$
Calcula el factorial de un número entero positivo que pedimos por teclado
Si tienes dudas de lo que es el factorial, consulta http://es.wikipedia.org/wiki/Factorial
"""

# Presentación
print "*" * 50
print "Programa que calcula el factorial de un número"
print "*" * 50

# Petición del número positivo
numero = int(raw_input("Introduzca un número positivo "))

while numero < 0:  # Aseguramos que el número es positivo
    numero = int(raw_input("Introduzca un número positivo "))    

# Por defecto: factorial de 0 es 1
factorial = 1

for n in range(1, numero + 1): # +1 porque si no range llegaría sólo hasta numero-1
    # n va tomando los valores desde 1 hasta numero
    factorial = factorial * n

print "El factorial del número", numero, "es", factorial


# Sugerencia: programa el bucle con un while y compara
