# -*- coding: cp1252 -*-
# $Id$
# $Author$

# Mensaje ayuda
print "Este programa muestra una frase al revés"

# Pedir datos
saludo = raw_input('Introduce una frase: ')

# Busco final
final = (len(saludo)+1)*-1

# Muestro frase al revés
# Range desde -1 hasta el tamaño de la frase(en negativo) menos 1
# El "paso" es negativo porque va descendiendo
for indice in range(-1, final, -1):
    print saludo[indice], # , para que no imprima el salto de línea
print 

# Ahora lo hacemos sin índices: concatenando las letras
alreves = "" # creamos nueva variable
for letra in saludo:
    alreves = letra + alreves
print "Segunda versión del programa"
print alreves
