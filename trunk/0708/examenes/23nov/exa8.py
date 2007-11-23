# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que tenga como parámetro un número entero y 
que devuelva True si el número es primo y False si no lo es.
"""

def esPrimo(n):
    for x in range(2, n**0.5 +1):
        if n % x == 0:
            return False
    return True

print esPrimo(8)
print esPrimo(9)
print esPrimo(13)
