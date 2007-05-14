# -*- coding: utf-8 -*-

# Cadenas HTML
# La página final se compondrá de encabezado + formulario + pie

_encabezado = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC  "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xml:lang="en" lang="en">
  <head>
    <title>Introducción a CherryPy</title>
    <meta content="text/html; charset=utf-8" />
  </head>
  <body>
"""
# fin de encabezado


_formulario = """
<form action="login" method="post">
    <p>Usuario</p>
    <input type="text" name="usuario" value="" 
        size="15" maxlength="40"/>
    <p>Contraseña</p>
    <input type="password" name="password" value="" 
        size="10" maxlength="40"/>
    <p><input type="submit" value="Login"/></p>
    <p><input type="reset" value="Borrar"/></p>
</form>
<p><pre>cherrypy/cherrypy</pre> si quieres tener éxito</p>
"""
# fin de formulario


_pie = """</body></html>"""


_acierto = """<h1 style="color:blue">OK</h1>"""

_error = """<h1 style="color:red">ERROR</h1><p><a href="/">Volver al formulario</a>"""



import cherrypy


class Root(object):
    def index(self):
        return _encabezado + _formulario + _pie
    index.exposed = True
    def login(self, usuario, password):
        """ Comprueba los permisos del ususario"""
        if usuario=='cherrypy' and password=='cherrypy':
            return _encabezado + _acierto + _pie
        else:
            return _encabezado + _error + _pie
    login.exposed = True
    
cherrypy.quickstart(Root())
    
