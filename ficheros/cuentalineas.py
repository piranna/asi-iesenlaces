# $Id$
### programa cuentalíneas

fichero = raw_input('Introduzca el nombre del fichero: ')
# Abre en modo lectura
# Si no ponemos modo: 'r' o mejor 'rt'
f = open(fichero)
# Inicializa contador
nlinea = 0

# Bucle para contar las líneas
for linea in f.readlines():
    nlinea +=1
    
# Imprime resultado
print 'El fichero', fichero, 'tiene', nlinea, 'lineas.'
