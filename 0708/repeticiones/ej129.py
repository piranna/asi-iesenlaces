# -*- coding: utf-8 -*-
"""
$Id$

Haz un programa que calcule el máximo comun divisor (mcd)
de dos enteros positivos.
El mcd es el número más grande que divide exactamente a ambos numeros.

Documentación: http://es.wikipedia.org/wiki/M%C3%A1ximo_com%C3%BAn_divisor
"""

# Presentación
print "*" * 50
print "Programa máximo común divisor"
print "*" * 50

# AVISO: falta validar que so positivos
numero1 = int(raw_input("Introduce el primer número: "))
numero2 = int(raw_input("Introduce el segundo número: "))


# prueba a sustituir esto por una sentencia con if
mayor = max(numero1, numero2)
menor = min(numero1, numero2)

candidato = 1
for valor in range(2, menor + 1):
    if mayor % valor == 0 and menor % valor == 0:
        candidato = valor
print "El mcd de %d y %d es %d" % (numero1, numero2, candidato)


"""
Propuesta: implementar el algoritmo de euclides:
http://es.wikipedia.org/wiki/Algoritmo_de_Euclides
"""
