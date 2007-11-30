# -*- coding: cp1252 -*-
"""
Escribe una función estaEn(lista, elemento) que
devuelva Verdadero si ese elemento está dentro de la lista
"""

def estaEn(lista, x):
    for el in lista:
        if el == x:
            return True
    return False
    
milista =  [4,5,6,7,3,4,5,6,4,5,6]

print ' T F T'
print estaEn(milista, 4)
print estaEn(milista, 44)
print estaEn(milista, 7)
