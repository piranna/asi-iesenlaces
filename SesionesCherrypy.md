# Sesiones con cherrypy #

Las sesiones se almacenan en un diccionario: `cherrypy.session`

Hay que activar el uso de sesiones con : `_cp_config = {'tools.sessions.on': True`}

Ejemplo: contador
```
#!python
# -*- coding: utf-8 -*-

import cherrypy

class Contador:
    _cp_config = {'tools.sessions.on': True}
    def index(self):
        # Incrementa el contador cada vez que se carga la página
        veces = cherrypy.session.get('contador', 0) + 1
        
        # almacena el nuevo valor en el diccionario session
        cherrypy.session['contador'] = veces
        
        # Muestra el mensaje
        return '''
            En la sesión actual has visto la página
            %s veces.
        ''' % veces
    index.exposed = True

cherrypy.quickstart(Contador())
```