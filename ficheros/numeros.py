# -*- coding: cp1252 -*-
# Escribe los números del 1 al 1000

f = open('numeros.txt', 'w')  # abrimos para escritura: creamos si no existe

linea = "%4d\n"   # cadena que voy a escribir en el fichero

for num in range(1, 1001):
	f.write(linea % num)
	
f.close()
