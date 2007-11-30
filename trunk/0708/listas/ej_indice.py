# -*- coding: cp1252 -*-
"""
Escribe una función indice(lista, elemento)
que devuelva la posición del elemento en la lista.
Si el elemento no está en la lista devolverá -1
"""


def indice(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    # No lo he encontrado :-(
    return -1

def indice2(lista, x):
    i = 0
    for el in lista:
        if el == x:
            return i
        i = i+1
    return -1


        

milista =  [4,5,6,7,3,4,5,6,4,5,6]

print "Tiene que salir: 0, -1, 3"
print indice(milista, 4)
print indice(milista, 44)
print indice(milista, 7)
print indice2(milista, 4)
print indice2(milista, 44)
print indice2(milista, 7)
