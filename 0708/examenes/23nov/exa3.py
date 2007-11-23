# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que tenga como parámetro una lista de números decimales
y devuelva la lista ordenada de mayor a menor.
"""

listaej = [4.5, 3.2, 99.5, 10.4, -5]


def ordenaReves(lista):
    lista.sort(reverse=True)
    return lista

def ordenaReves2(lista):
    lista.sort()
    lista.reverse()
    return lista

def ordenaReves3(lista):
    for x in range(1, len(lista)):
        for y in range(len(lista)-x):
            if lista[y] < lista[y+1]:
                lista[y], lista[y+1] = lista[y+1], lista[y]
                # forma estándar de intercambiar
                #aux = lista[y]
                #lista[y] = lista[y+1]
                #lista[y+1] = aux
    return lista

            
            


print ordenaReves(listaej[:])

print ordenaReves2(listaej[:])

print ordenaReves3(listaej[:])