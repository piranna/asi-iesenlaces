import cherrypy
import os, glob

"""
Mezclando contenido estático y dinámico
Más info en http://www.cherrypy.org/wiki/StaticContent
y http://tools.cherrypy.org/wiki/MixingStaticAndDynamicContent
"""


class EstaticoYDinamico(object):
    dir_actual = os.path.abspath(os.path.dirname(__file__))
    _cp_config = {'tools.staticdir.on' : True,
                  'tools.staticdir.dir' : dir_actual,
                  'tools.staticdir.index' : 'ejemplo_estatico.html',
    }

    @cherrypy.expose
    def ejercicios(self):
        contenido = "<h1>Listado del directorio</h1>"
        linea = """<li><a href="%s">%s</a></li>"""
        archivos = glob.glob("*.py")
        yield(contenido + '<ol>')
        for archivo in archivos:
            yield(linea % (archivo, archivo))
        yield('</ol>')
        yield('<hr /><p><a href="/">Volver</a></p>')

cherrypy.quickstart(EstaticoYDinamico())
