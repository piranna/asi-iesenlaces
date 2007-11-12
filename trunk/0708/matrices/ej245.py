# -*- coding: cp1252 -*-
#$Id$

"""
Una matriz identidad es aquella cuyos elementos en la diagonal principal, es decir,
accesibles con una expresión de la forma M[i][i], valen uno y el resto valen cero. Construye
una matriz identidad de 4 filas y 4 columnas.
"""
from pprint import pprint

M = []

for i in range(4):
    aux = [0]* 4
    M.append(aux)
    M[i][i] = 1
pprint (M)


