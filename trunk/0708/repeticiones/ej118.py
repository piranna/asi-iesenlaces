# -*- coding: utf-8 -*-
"""
$Id$

Realiza un programa que proporcione el desglose en billetes y monedas de
una cantidad entera de euros. Recuerda que hay billetes de 500, 200, 100,
50, 20, 10 y 5 € y monedas de 2 y 1 €.
Debes recorrer los valores de billete y moneda disponibles con uno o más
bucles for-in.
"""

# Presentación
print "*" * 50
print "Desglose de billetes"
print "*" * 50

# Petición de la cantidad
cantidad = int(raw_input("Introduzca un número positivo "))

# Variable para evitar tantas repeticiones
billetes = [500, 200, 100, 50, 20, 10, 5] 

for billete in billetes:
    parcial = cantidad / billete  # división entera: x billetes de billete
    if parcial:
        print parcial, "billetes de", billete, "euros"
    cantidad = cantidad % billete  # actualizamos la cantidad que queda por repartir
    
parcial = cantidad / 2
if parcial:
    print parcial, "monedas de 2 euros"
    cantidad = cantidad % 2
if cantidad:
    print cantidad, "monedas de 1 euro"

