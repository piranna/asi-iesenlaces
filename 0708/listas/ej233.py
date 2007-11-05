# -*- coding: utf-8 -*-

# $Id$
# elimina números pares de una lista

"""
Eliminamos elementos de una lista con del().
Cuidado al eliminar elementos de una lista.
Si eliminamos un elemento de una lista, estamos
modificando su tamaño
"""


lista = [1,2,3,4,5,6,7,8,9]

i=0  #índice para recorrer la lista

while i < len (lista):
    # en cada iteración volvemos a evaluar el tamaño de la lista
    if lista[i] % 2 == 0:
        del lista[i]
    else:
        i += 1
        # sólo modificamos el índice cuando no eliminamos ningún elemento
        # si hemos eliminado un elemento no es necesario, porque el índice ahora
        # apunta al siguiente (el que ocupa el nuevo lugar del eliminado)

print lista

