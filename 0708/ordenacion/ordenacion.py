# -*- encoding: utf-8 -*-
# $Id$

# ejemplos de ordenación
from pprint import pprint

lista = [1, 5,3 ,85 ,30 , 23, 54]

# ordenación normal de la lista
# la ordenación es dinámica (la lista se ordena). IMPORTANTE: no hay que 
# asignar de nuevo la lista. Sort() devuelve None
lista.sort()
pprint(lista)

# para ordenar en orden inverso
lista.sort(reverse=True)
pprint(lista)

nombres = ['Martínez, Blanca', 'Blasco, Pilar', 'García, Alberto']

# ordenación normal:
nombres.sort()
pprint(nombres)

# ordenación inversa:
nombres.sort(reverse=True)
pprint(nombres)

# ordenación por el nombre

def nombreMayor(nom1, nom2):
    """
    nombreMayor(cadena, cadena)
    
    Compara dos cadenas con la estructura: apellido, nombre por el segundo
    elemento --> nombre
    """
    return cmp(nom1.split(',')[-1].strip(), nom2.split(',')[-1].strip())

nombres.sort(cmp=nombreMayor)

pprint(nombres)