# -*- coding: utf-8 -*-

import amara

# creo objeto parseado
doc = amara.parse('http://www.ies-losenlaces.com/ci/file.php/7/ejercicios/listado.html')

# puedo comprobar que lo leo bien
# print doc.xml(encoding='iso-8859-1')

# Documento destino:
fout = file('salida.html', 'w')
fout.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Ejercicio de clase</title>
<meta http-equiv=Content-Type content="text/html; charset=utf-8" />
</head>
<body>""")


# titulo:
fout.write('<para>El título de la página es "%s"</para>' % unicode(doc.html.head.title).encode('utf-8'))

# ponentes (nombres en mayúsculas)
def convertir(nomCompleto):
    lista = nomCompleto.split(' ', 1)
    return lista[0] + ' ' + lista[1].upper()

fout.write('<h2>Lista de ponentes</h2>\n<ol>')
for li in doc.html.body.ol.li:  # recorre los distintos li de ol
    fout.write('<li>%s</li>' % convertir(unicode(li).encode('latin1')))
fout.write('</ol>')

# Descargar imagen a un archivo local
import urllib
src_imagen = doc.html.body.img.src
f_img = open('foto.jpg', 'w').write(urllib.urlopen(src_imagen).read())

('\n</body>\n</html>')
fout.close()
