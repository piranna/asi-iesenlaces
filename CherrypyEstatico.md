# Contenido estático #

Con los métodos de CherryPy se sirven documentos dinámicos. Si necesitamos servir documentos estáticos (**css, js, imágenes, ...**) hay que modificar la configuración del servidor.
## Servir ficheros aislados ##
**staticfile**
```
directorio_actual = os.path.abspath(os.path.dirname(__file__))
conf = { '/': {'tools.saticfile.root': directorio_actual},
         '/css/style.css': {tools.staticfile.on': True, 
                            tools.staticfile.filename': 'nombre_css.css'
                           }
       }
cherrypy.quickstart(MiPrograma(), config=conf)
```

## Servir directorios completos ##
**staticdir**
```
directorio_actual = os.path.abspath(os.path.dirname(__file__))
conf = { '/': {'tools.saticdir.root': directorio_actual},
         '/css': {tools.staticdir.on': True, 
                  tools.staticdir.dir': os.path.join(directorio_actual, 'dir_css')
                 }
       }
cherrypy.quickstart(MiPrograma(), config=conf)
```
Se establece la correspondencia entre el directorio físico del servidor y el directorio que aparece en el html/xhtml.