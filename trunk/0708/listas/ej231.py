# -*- coding: cp1252 -*-
#$Id$

"""
Diseña un programa que lea una cadena y muestre por pantalla una lista con todas sus
palabras en minúsculas. La lista devuelta no debe contener palabras repetidas.
"""
cadena = raw_input("Introduzca una frase: ")

minusculas = []

for palabra in cadena.split():
    # recorre frase partida en palabras.
    # sólo añade as minúsculas que no estaban antes en la lista minusculas
    if palabra.islower() and palabra not in minusculas:
        minusculas.append(palabra)

print minusculas
