# -*- coding: cp1252 -*-
"""
$Id$
Ej 113
Pide un texto que no tenga mayúsculas. Si hay una letra mayúscula,
vuelve a pedir el texto
"""

texto = raw_input("Introduce una frase toda en minúsculas: ")
while not texto.islower():
    # vuelve a pedir el texto si hay alguna mayúscula
    texto = raw_input("Introduce una frase toda en minúsculas: ")
print "Texto introducido", texto
