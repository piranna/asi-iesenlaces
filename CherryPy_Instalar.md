# Instalación #

## Instalar desde el código fuente ##
  * Descargar el código del repositorio: http://download.cherrypy.org/cherrypy/  (la última versión está en http://download.cherrypy.org/cherrypy/3.0.1/CherryPy-3.0.1.tar.gz)
  * Descomprimir en un directorio
  * Ejecutar `python setup.py install`

## Con setuptools ##
  * Si no está instalado setuptools descargar **ez\_setup.py** (http://peak.telecommunity.com/dist/ez_setup.py) y ejecutar el archivo `python ez_setup.py`
  * `easy_install -U cherrypy` En windows, si python no está en el path del sistema: `C:\Python25\Scripts\easy_install.exe -U cherrypy`

**Comprobación**
```
$ python
>>> import cherrypy
>>> cherrypy.version
>>> cherrypy.__version__
'3.0.1'
>>>
```