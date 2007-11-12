# -*- coding: cp1252 -*-
#$Id$
"""
Diseña un programa que lea una lista de 10 enteros, pero asegurándose de que todos
los números introducidos por el usuario son positivos. Cuando un número sea negativo, lo
indicaremos con un mensaje y permitiremos al usuario repetir el intento cuantas veces sea
preciso.
"""

lista = []
for x in range (10):
    num = int(raw_input("Introduce un numero: "))
    while num < 0: # si el número introducido es negativo, vuelve a pedirlo
        num = int(raw_input("Introduce un numero: "))
    lista.append(num)

print lista
