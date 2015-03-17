# Cherrypy #

Cherrypy (http://www.cherrypy.org/) es una librería para desarrollar aplicaciones web con python, que no exige un conocimiento del protocolo http. Las aplicaciones web se desarrollan como el resto de programas orientados a objetos con python.

## Instalación ##
Si no está instalado, ve a CherryPy\_Instalar e instálalo.

## Hola mundo ##
Escribimos nuestro primer programa: una clase con un método index.html. Ese método tiene que ser accesible (**exposed**). `quickstart(HolaMundo())` publica una instancia de la clase `HolaMundo` y lanza el servidor web. Podremos parar el servidor con `Ctrl+C`:
```
# -*- coding: utf-8 -*-


import cherrypy

class HolaMundo:
    def index(self):
        return "¡Hola, mundo!"
    index.exposed = True
    
cherrypy.quickstart(HolaMundo())
```
Ejecutamos la aplicación. Vemos que por defecto sirve en el puerto 8080, al que dirigiremos nuestro navegador con `http://localhost:8080`:
```
$ python holaMundo.py
[14/May/2007:14:13:40] HTTP Serving HTTP on http://0.0.0.0:8080/
CherryPy Checker:
The Application mounted at '' has an empty config.
```

El servidor web traducirá la dirección a peticiones de objetos. Veamos un caso más complejo. Podremos acceder a ` /, /despedida y /pregunta`:
```
# -*- coding: utf-8 -*-

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
```

## Más ##
  * [Contenido estático](CherrypyEstatico.md)
  * [Uso de sesiones](SesionesCherrypy.md)
  * [Fuentes y ejemplos de clase](http://asi-iesenlaces.googlecode.com/svn/trunk/cherrypy/)
  * [CherryPy\_XmlRpc](CherryPy_XmlRpc.md)
  * [Configurando el Servidor](Cherrypy_Configuracion.md)