# -*- coding: utf-8 -*-

# Cadenas HTML

formulario = """
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

acierto = """<h1 style="color:blue">OK</h1>"""

error = """<h1 style="color:red">ERROR</h1><p><a href="/">Volver al formulario</a>"""

import cherrypy


class Root(object):
    def index(self):
        return formulario
    index.exposed = True
    def login(self, usuario, password):
        """ Comprueba los permisos del ususario"""
        if usuario=='cherrypy' and password=='cherrypy':
            return acierto
        else:
            return error
    login.exposed = True
    
cherrypy.quickstart(Root())
    
