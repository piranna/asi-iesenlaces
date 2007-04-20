# -*- coding: cp1252 -*-
# $Id$
# $Author$

# Pido frase
frase = raw_input('Introduzca una frase: ')

# Cuento vocales
VOCALES = 'aeiouAEIOUáéíóúAÉÍÓÚ'
num_vocales = 0  # creamos / inicializamos contador
for letra in frase:
    if letra in VOCALES:
        num_vocales = num_vocales + 1

# Muestro resultado
print 'Hay', num_vocales, 'vocales.'
