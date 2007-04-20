# $Id$

# Ejercicio cuentaletras

fichero = raw_input('Introduzca el nombre del fichero: ')

# fichero abierto en modo lectura
f = open(fichero, 'r')

letras = 0

# leo el fichero y proceso la cadena de caracteres
"""
for letra in f.read():
    if letra.isalnum():
        letras += 1
"""
letra = f.read(1)
while letra:
    if letra.isalnum():
        letras += 1
    letra = f.read(1)
    
        
print 'El fichero', fichero, 'tiene', letras, 'letras.'

raw_input()
