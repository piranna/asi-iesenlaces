# -*- coding: utf-8 -*-


# instalar antes cherrypy si no está instalado con
# $ easy_install -U cherrypy
import cherrypy

class Despedida(object):
    def index(self):
        return "¡¡¡Hasta luego!!!"
    index.exposed = True

class HolaMundo(object):
    despedida = Despedida()
    def index(self):
        return "¡Hola, mundo!"
    index.exposed = True  # hace accesible el métido. Si no, no podríamos acceder a él.
    def pregunta(self):
        return("¿Cómo estás?")
    pregunta.exposed=True

# publica la clase HolaMundo
cherrypy.quickstart(HolaMundo())
