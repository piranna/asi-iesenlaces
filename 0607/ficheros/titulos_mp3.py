# -*- coding: cp1252 -*-

## muestra los títulos de las canciones que tengo en un directorio

import glob

directorio = r'\\Inf2-08\DATOS\*.mp3'  # cambiar por el correcto

# solo imprime en pantalla
for mp3 in glob.glob(directorio):
	f = open(mp3, 'rb')
	f.seek(-128,2)
	if f.read(3).upper() == 'TAG':
		print f.read(30).strip('\x00')
	f.close()

# escribiendo salida en fichero de texto
fsal = open('miscanciones.txt', 'w')
for mp3 in glob.glob(directorio):
	f = open(mp3, 'rb')
	f.seek(-128,2)
	if f.read(3).upper() == 'TAG':
		titulo = f.read(30).strip('\x00')
		artista = f.read(30).strip('\x00')
		disco = f.read(30).strip('\x00')
		year = f.read(4)
		fsal.write("%-30s %-30s %-30s %-6s\n" % (artista, titulo, disco , year) )
	f.close()
fsal.close()

# escribiendo etiquetas html
fsal = open('miscanciones.html', 'w')
fsal.write('<html><body><h1>Mis canciones</h1><table border="1">')
for mp3 in glob.glob(directorio):
	f = open(mp3, 'rb')
	f.seek(-128,2)
	if f.read(3).upper() == 'TAG':
		titulo = f.read(30).strip('\x00')
		artista = f.read(30).strip('\x00')
		disco = f.read(30).strip('\x00')
		year = f.read(4)
		fsal.write("""<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>\n""" % (mp3, artista, titulo, disco , year) )
	f.close()
fsal.write('</table></body></html>')
fsal.close()









