# -*- coding: utf-8 -*-
"""
$Id$

Calcula si un número es primo. Ej. pág 118.

Hay que mejorar el algoritmo. 
"""

num = int(raw_input("Introduzca un número: "))

creo_que_es_primo = True

for divisor in range (2, num ):
    if num % divisor == 0:
          creo_que_es_primo = False
    # Esta parte necesita una mejora. Prueba con un número muy grande

# creo_que_es_primo ya es un booleano.
# No es necesario compararlo creo_que_es_primo == True
if creo_que_es_primo:
    print 'El número', num ,'es primo'
else:
    print 'El número', num ,'no es primo'
