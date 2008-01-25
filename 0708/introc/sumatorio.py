# -*- coding: utf-8 -*-
from math import *

# Pedir l´ımites inferior y superior.

a = int(raw_input('Límite inferior: '))

while a < 0:
    print 'No puede ser negativo'
    a = int(raw_input('Límite inferior: '))
    
b = int(raw_input('Límite superior:'))
while b < a:
    print 'No puede ser menor que %d' % a
    b = int(raw_input('Límite superior:'))

# Calcular el sumatorio de la ra´ız cuadrada de i para i entre a y b.
s = 0.0

for i in range(a, b+1):
    s += sqrt(i)

# Mostrar el resultado.
print 'Sumatorio de raíces',
print 'de %d a %d: %.2f' % (a, b, s)







