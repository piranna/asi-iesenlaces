# -*- coding: utf-8 -*-
import cherrypy
from cherrypy import _cptools

class Root:
    @cherrypy.expose
    def index(slef):
        return "Esto es una página web"

class MisFunciones(_cptools.XMLRPCController):
    @cherrypy.expose
    def mayusculas(self, mensaje):
        return mensaje.upper()
    @cherrypy.expose
    def suma(self, x, y):
        return x + y

root = Root()
root.xmlrpc = MisFunciones()
cherrypy.quickstart(root, '/')
