# -*- coding: cp1252 -*-
# Escribe los números del 1 al 10000


###### primera parte: escribe 10000 números
f = open('numeros.txt', 'w')  # abrimos para escritura: creamos si no existe

linea = "%d\n"   # cadena que voy a escribir en el fichero

for num in range(1, 10001):
	f.write(linea % num)
	
f.close()  # cierro para escritura


###### segunda parte: leer y escribir

flec = open('numeros.txt', 'r') # fichero origen: lectura

for i in range(1, 11):
    # abrir en modo escritura
    print 'Escribiendo fichero numeros_%d.txt' % i  # si queremos ver algo en pantalla
    fesc = open('numeros_%d.txt' % i, 'w')
    # proceso: leer ---> escribir
    for x in range(1000):
        linea = flec.readline()
        fesc.write(linea)
        # fesc.write( flec.readline() )
    # cerrar
    fesc.close()
flec.close()










