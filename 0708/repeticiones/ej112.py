# -*- coding: cp1252 -*-
"""
Ej 112.
Solicita un número entre 0 y 10 (ambos incluidos)
"""

numero = int(raw_input("Introduzca un número: "))

while numero < 0 or numero > 10:
    # vuelve a pedir el número si está mal
    numero = int(raw_input("Introduzca un número: "))
    
print "Numero introducido: ", numero

raw_input("Pulsa intro para continuar ")
