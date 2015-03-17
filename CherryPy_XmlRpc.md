# XML-RPC #

**Servidor**
```
# -*- coding: utf-8 -*-
import cherrypy
from cherrypy import _cptools

class Root:
    @cherrypy.expose
    def index(slef):
        return "Esto es una página web"

class MisFunciones(_cptools.XMLRPCController):
    """Batería de funciones accesibles por xml-rpc"""
    @cherrypy.expose
    def mayusculas(self, mensaje):
        return mensaje.upper()

    @cherrypy.expose
    def suma(self, x, y):
        return x + y


root = Root()
root.xmlrpc = MisFunciones()
cherrypy.quickstart(root, '/')
```
**Cliente**
```
import xmlrpclib

s = xmlrpclib.ServerProxy("http://localhost:8080/xmlrpc/")

print s.suma(10, 15)
print s.mayusculas('hola')
```


Propuesta de ejercicios interesantes en http://www.cs.huji.ac.il/~sclass/exercises/ex3.html