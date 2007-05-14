# -*- coding: utf-8 -*-

# Cadenas HTML
# La página final se compondrá de encabezado + cuerpo + pie

_encabezado = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC  "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xml:lang="en" lang="en">
  <head>
    <title>IP's del aula de programacion</title>
    <meta content="text/html; charset=utf-8" />
    <style type="text/css">
     li {
       float:left;
       width: 10em;
       list-style:none;
     }
     a {
      text-decoration:none;
      }
     
     a:hover {
        color:red;
        border: solid thin red;
        }

    </style>
  </head>
  <body>
"""
# fin de encabezado

_pie = """</body></html>"""


import cherrypy


class Root(object):
    def index(self):
        ip_inicio = 1
        ip_fin = 50
        rango="172.30.6.%d"
        cuerpo = "<h1>Equipos del aula de informática</h1>\n<ul>"
        for num in range(ip_inicio, ip_fin+1):
            ip = rango % num
            cuerpo += """<li><a href="http://%s">%s</a></li>\n""" % (ip, ip)
        cuerpo += "</ul>"
        return _encabezado + cuerpo + _pie
    index.exposed = True
        
cherrypy.quickstart(Root())
    
