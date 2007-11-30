# -*- coding: cp1252 -*-
# $Id$
"""
Escribe una funcion contar(lista, elemento) que devuelva
el número de veces que aparece ese elemento en la lista.
Fíjate en la función
"""

def contar(lista, elemento):
    nveces = 0
    for x in lista:
        if x == elemento:
            nveces += 1
    return nveces

# test del ejercicio
milista =  [4,5,6,7,3,4,5,6,4,5,6]
print contar(milista, 5) , 'bien --> 3'
print contar(milista, 55) , 'bien --> 0'
print contar(milista, 3) , 'bien --> 1'
