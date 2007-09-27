# -*- coding: cp1252 -*-
#$Id$

"""
Dice si un año es bisiesto o no
"""

# Pedir año
anno = input("Introduzca el año: ")

# cacular si es bisiesto y mostrar

if (not anno%400) or (anno % 4 == 0 and anno % 100):
    salida = "es bisiesto"
else:
    salida = "no es bisiesto"

print 'El año', anno, salida
