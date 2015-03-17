# Múltiples versiones de un paquete #

A veces nos interesa (por problemas de dependencias) tener instaladas varias versiones de un mismo paquete.
A easy install le podemos indicar que haga una instalación multiversión con el parámetro `-m`. Por ejemplo:
```
$ easy_install -m Cherrypy
```

Luego podemos usar en el código
```
pkg_resources.require("CherryPy")         # última versión instalada
pkg_resources.require("CherryPy==3.0.1")  # Esta versión exacta
pkg_resources.require("CherryPy>=3.0.1")  # Esta versión o mayor
pkg_resources.require("CherryPy<3")       # Menor que esta versión
```