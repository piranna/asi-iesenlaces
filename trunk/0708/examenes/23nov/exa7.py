# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que reciba como parámetro una lista de enteros 
y que imprima en pantalla el número mayor, el menor y la media.
"""

def muestraLista(lista):
    lista.sort()
    print 'El mayor es', lista[-1]
    print 'El menor es', lista[0]
    print 'La media es', sum(lista) / len(lista)

def muestraLista2(lista):
    if not lista:
        print 'lista vacía'
    else:
        menor = lista[0]
        mayor = lista[0]
        total = 0
        for n in lista:
            if n > mayor:
                mayor = n
            if n < menor:
                menor = n
            total += n
        print 'El mayor es', mayor
        print 'El menor es', menor
        print 'La media es', total/len(lista)
    
        


muestraLista(range(11))
muestraLista([4,8,111,-9])
muestraLista2(range(11))
muestraLista2([4,8,111,-9])