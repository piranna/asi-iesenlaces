# -*- coding: utf-8 -*-

# Cadenas HTML
# La página final se compondrá de encabezado + cuerpo + pie

_encabezado = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC  "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xml:lang="en" lang="en">
  <head>
    <title>Album de fotos</title>
    <meta content="text/html; charset=utf-8" />
  </head>
  <body>
"""
# fin de encabezado

_pie = """</body></html>"""

import os
import cherrypy


class Root(object):
    def index(self):
        contenido ="<h1>Album de fotos</h1>\n<p>Directorios estáticos en acción</p>"
        for imagen in os.listdir('imagenes'):
            contenido += """<img src="img/%s" alt="imagen %s" />\n""" % (imagen, imagen)
        return _encabezado + contenido + _pie
    index.exposed = True

# preparación configuración
directorio_actual = os.path.abspath(os.path.dirname(__file__))
conf = { '/': {'tools.saticdir.root': directorio_actual},
         '/img': {'tools.staticdir.on': True, 
                  'tools.staticdir.dir': os.path.join(directorio_actual, 'imagenes')
                 }
       }

# Arranque aplicación
cherrypy.quickstart(Root(), config=conf)
