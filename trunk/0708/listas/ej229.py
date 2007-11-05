# -*- coding: utf-8 -*-
# $Id$

"""
Diseña un programa que construya una lista con los n primeros numeros primos
"""

cuantos = int(raw_input("Cuántos números primos tengo que buscar? "))

listaPrimos = []

n=2

while len(listaPrimos) < cuantos:
    if n == 2:
        listaPrimos.append(n)
        n+=1
        # El 2, primer número par.
    else:
        # voy a mirar el resto de número impares
        esPrimo = True
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                esPrimo = False
        if esPrimo:
            listaPrimos.append(n)
        n+=2

print listaPrimos
