# Introducción al uso de MochiKit #

MochiKit (www.mochikit.com) es una librería javascrip escrita al estilo Python. Tiene herramientas para gestionar AJAX, DOM, programación funciona, fechas, formato de cadenas, colores, efectos visuales, eventos, y muchas otras prestaciones. MochiKit 1.3 funciona con  Safari 2.0.2, Firefox (1.0.7, 1.5 y 2.0), Opera 8.5 e Internet Explorer (6 y 7). La documentación es abundante y tiene una batería de tests muy completa.


## Descarga e instalación ##
Instrucciones de descarga en http://mochikit.com/download.html

Se puede descargar la última versión estable (http://mochikit.com/dist/MochiKit-1.3.1.zip) o la versión en desarrollo:
```
svn co http://svn.mochikit.com/mochikit/trunk mochikit
```
Se copiará en un directorio accesible desde el servidor web que estemos utilizando (o en un directorio local si no se accede por `http`)

## Uso ##
Para usar la librería se incluirá una etiqueta script que acceda al archivo MochiKit.js, además del que acceda a las funciones que estemos programando nosotros.
```
<script type="text/javascript" src="../MochiKit/MochiKit.js" />
<script type="text/javascript" src="misfunciones.js" />
```
**Importante**: hay que poner bien la ruta de donde hemos descargado la librería y las mayúsculas: **M** ochi **K** it.

## Documentación ##
  * http://mochikit.com/doc/html/MochiKit/index.html
  * http://svn.mochikit.com/presentations/2006/ajax_experience/slides.html
  * Recopilación de frameworks:
    * http://www.gloo.ru/c/Survey-of-AJAX-JavaScript-Libraries/es.html.aspx
    * http://www.sitepoint.com/article/javascript-library

## Ejemplos ##
  * EsquinasRedondeadasConMochikit
  * [Introducción al DOM con MochiKit](MochikitDom.md)
  * [Tablas que se pueden ordenar](OrdenaTablas.md)