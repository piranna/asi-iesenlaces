# -*- encoding: utf-8 -*-
# $Id$

"""
Ejemplo de ordenación de una lista usando el método de la 
burbuja. En este caso ordenamos una lista de nombres
"""

from pprint import pprint
lista = ['Pepe', 'Juan', 'María', 'Ana', 'Luis', 'Pedro']

for i in range(1, len(lista)):
      for j in range(0, len(lista)-i):
         if lista[j] > lista[j+1]:  # compara y si es necesario, intercambia
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento

pprint(lista) 