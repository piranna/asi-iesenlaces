# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que tenga como parámetro una lista de enteros y 
que devuelva la lista una vez eliminados los números pares.
"""


def sinPar(lista):
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            del(lista[i])
        else:
            i += 1
    return lista

print sinPar(range(50))

