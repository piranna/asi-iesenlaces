# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que reciba como parámetro una matriz y que 
imprima en la pantalla cuántas y filas y cuántas columnas tiene
"""

def analizaMatriz(matriz):
    print 'filas', len(matriz), 'columnas', len(matriz[0])

analizaMatriz([[1,2,3,4],[5,6,7,8]])

analizaMatriz([[1,2], [3,4], [5,6], [7,8]])
                  