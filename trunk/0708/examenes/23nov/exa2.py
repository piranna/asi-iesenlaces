# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe un programa que pida una serie de números. La serie acaba cuando 
el usuario introduzca un número negativo. A continuación el programa 
mostrará la serie de números introducidos.
"""

numero = int(raw_input("Introduzca un número: "))
numeros = []

while numero >= 0:
    # guardo en la lista números sólo los válidos para mostrarlos luego
    numeros.append(numero)
    numero = int(raw_input("Introduzca un número: "))
    
for n in numeros:
    print n
