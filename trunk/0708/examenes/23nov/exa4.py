# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que reciba como parámetro una palabra, 
la imprima al revés y devuelva el número de vocales que tiene
"""

def alreves(palabra):
    vocales = 0
    inversa = ""
    for letra in palabra:
        if letra in 'aeiouAEIOU': # podríamos considerar también los acentos
            vocales += 1
        inversa = letra + inversa
    print inversa
    return vocales

print alreves('Hola carabola')
        