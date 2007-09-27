# -*- coding: cp1252 -*-
# $Id$

"""
Traduce nota numérica a Insuficiente, Suficiente ...
"""
# leer nota
nota = input('Introduzca nota numérica: ')

# calcular correspondencia
if nota < 5:
    resultado = "Insuficiente"
elif nota < 7:
    resultado = "Suficiente"
elif nota < 9:
    resultado = "Notable"
elif nota <=10:
    resultado = "Sobresaliente"
else:
    resultado ="NOTA INCORRECTA"
# mostrar resultado
print 'La nota', nota, 'es', resultado
