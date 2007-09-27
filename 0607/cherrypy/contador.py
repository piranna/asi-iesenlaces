# -*- coding: utf-8 -*-

import cherrypy

# variable global veces para usar en contador (malo)
veces = 0

class Contador:
    veces = 0
    _cp_config = {'tools.sessions.on': True}
    def index(self):
        # Muestra de dos contadores: uno malo y otro bueno.
        return """<h1>Ejemplo de contadores</h1>
        <p><a href="/bueno">Contador bueno (usa sesiones)</a></p>
        <p><a href="/malo">Contador malo (usa una variable de clase)</a></p>
        <p><a href="/otromalo">Contador malo (usa una variable global)</a></p>
        """
    index.exposed = True

    def bueno(self):
        # Incrementa el contador cada vez que se carga la página
        # si aún no se ha introducido la clave contador en el diccionario
        # de la sesión, devuelve 0
        veces = cherrypy.session.get('contador', 0) + 1
        
        # almacena el nuevo valor en el diccionario session
        cherrypy.session['contador'] = veces

        Contador.veces += 1
        # Muestra el mensaje
        return '''
            En la sesión actual has visto la página
            %s veces.
        ''' % veces
    bueno.exposed = True


    def malo(self):
        # Usa la variable de clase: veces
        # Comprobar accediendo desde distintos equipos
        Contador.veces += 1
        # Muestra el mensaje
        return '''
            En la sesión actual has visto la página
            %s veces.
        ''' % Contador.veces
    malo.exposed = True

    def otromalo(self):
        # Usa una variable global: veces
        # Comprobar accediendo desde distintos equipos
        global veces
        veces += 1
        # Muestra el mensaje
        return '''
            En la sesión actual has visto la página
            %s veces.
        ''' % veces
    otromalo.exposed = True
    


cherrypy.quickstart(Contador())

