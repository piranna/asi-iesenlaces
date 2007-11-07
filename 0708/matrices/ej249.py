# -*- coding: utf-8 -*-
"""
Matriz identidad de n x n

Pide un entero positivo n y almacena en una variable M la matriz
identidad de n × n (la que tiene unos en la diagonal principal y
ceros en el resto de celdas).
"""


import pprint # para mejorar la salida

# TAREA: se puede validar la entrada
n = int(raw_input("Introduzca un número positivo: ")) 
        
M = []

for i in range(n):
    aux = [0] * n    # crea fila de ceros
    M.append(aux)    # añade la fila
    M[i][i] = 1      # esto es lo peculiar de la matriz identidad.

pprint.pprint(M)     # muestra resultado
 
