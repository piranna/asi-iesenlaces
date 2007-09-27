# -*- coding: cp1252 -*-
# $Id$
"""
Imprime los múltiplos de un número que introduce el usuario,
menores que un número que introduce el mismo
"""
limite = input('Introduzca el número hasta el que ver la serie: ')
base = raw_input('Introduzca números para ver múltiplos: ')  # Primer número
base = int(base)
num = base

while num < limite:
    print num
    num = num + base
    

