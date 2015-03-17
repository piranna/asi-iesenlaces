# Configuración del Servidor #

Cherrypy tiene su propio sistema de configuración.
Se puede configurar de dos formas:

## Con un diccionario ##
```
global_conf = {
    'global' : {
         'server.socket_host': 'localhost',
         'server.socket_port': 8080,
     },
}
application_conf = {
    '/estilo.css': {
          'tools.staticfile.on': True,
          'tools.staticfile.filename': os.path.join(_curdir, 'estilo.css'),
     }
}

[ ... ]
cherrypy.config.update(global_conf)
```

## Con un archivo ##
```
[global]

server.socket_host="localhost"
server.socket_port=8080

[/estilo.css]
tools.staticfile.on=True
tools.staticfile.filename="/ruta/a/mi/archivo/estilo.css"

[ ... ]

cherrypy.config.update('/path/del/archivo.conf')

```

## _cp\_config ##
También se puede usar el atributo `_cp_config`_

```
_cp_config = {'tools.gzip.on': True}
```