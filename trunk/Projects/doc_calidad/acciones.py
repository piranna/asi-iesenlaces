# -*- coding: cp1252 -*-
"""
(c) lm morillas 2008
Crea un html con la información del archivo de acciones abiertas.

1. Punto de partida: archivo .xls de excel con información de acciones abiertas
2. Se crea el archivo .csv eliminando filas vacías o sin contenido válido. La primera fila son las cabeceras de las columnas. Se eliminan también las columnas vacías.
3. El programa crea "a pelo" un html. Se imprime, para luego poderlo redirigir.
4. La primera columna contendrá los enlaces a los archivos, que estarán en un directorio recogido por la variable path_archivos.
5. Forma de uso:
    * el archivo .csv se llamará acciones_calidad.csv, en el mismo directorio que el programa.
    * configurar el path
    * ejecutar python acciones.py > acciones.html

"""

import os, glob
import csv

# IMPORTANTE: path donde están los documentos
PATH_ARCHIVOS = r'acciones de mejora'

# Abrir con cvs el archivo
f = csv.reader(open('acciones_calidad.csv'))

# Lista de acciones. La primera fila serán los títulos
acciones = []

for l in f:
    acciones.append(l)

# Separo títulos
titulos =  acciones[0]

# Acciones de mejora
acciones = acciones[1:]

# Composición del html
titulo = "Listado de acciones correctivas, preventivas o de mejora"
doc = """<html>
 <head>
    <title>%s</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="layout.css" type="text/css"/>
  </head>
    <body><h1>%s</h1><p>&nbsp;</p><div id="datos">""" % (titulo, titulo)
tabla = '<table class="tabla">\n<tr>'

# Los títulos van en un <th>
for c in titulos:
    tabla += '<th>%s</th>' % c
tabla += '</tr>'

# Filas para las acciones que NO están CERRADAS
for accion in acciones:
    accion = [a.replace('"', '') for a in accion]
    if not accion[5] == 'Cerrada':
        codigo = accion[0]
        fila = '<tr>\n'
        ruta = glob.glob(os.path.join(PATH_ARCHIVOS,codigo.replace('/', '_')+'*'))
        if ruta:
            ruta = ruta[0]
        # si no se encuentra la ruta del archivo
        else: ruta="error"  

        celda = '<td><a href="%s" target="_blank">%s</a></td>\n' % (ruta, codigo)

        fila += celda
        for acc in accion[1:]:
            celda = '<td>%s</td>\n' % acc
            fila += celda
        fila += '</tr>\n'
        tabla += fila
tabla += '</tabla></div>'
                
# Al final imprime el doc .html                
print doc + tabla +'</body></html>'
