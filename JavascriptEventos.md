# Eventos #

Programación orientada a eventos. Los eventos son acciones que ocurren porque el usuario hace algo sobre un objeto (un clic, introducir texto, mover el ratón ...)

Los eventos se capturan mediante los manejadores de eventos (handler). El proceso a realizar se programa mediante funciones JavaScript llamadas por los manejadores de eventos.

## Algunos eventos ##

| **evento** | **manejador** | **Ocurre cuando ...** |
|:-----------|:--------------|:----------------------|
| abort | onabort | abortar la carga de una imagen |
| blur | onblur |cambiar el foco a otro elemento|
|click | onclick | hacer click en algo|
| change| onchange |cambiar el valor de un elemento |
|error | onerror |la carga de un bloque causa un error |
|focus | onfocus| pasar el foco a otro elemento|
| load|onload |el usuario carga la página |
|mouseout |onmouseout |  |
|mouseover |onmouseover |  |
|reset |onreset |  |
|select | onselect |  |
|submit |onsubmit |  |
|unload | onunload| El usuario sale de la página |

## Definir manejador ##
```
 <form onreset="return confirm('¿Estás seguro?')" ...>
```

**Valor de retorno** : Puede anular el comportamiento por defecto de los eventos. Ejemplo: validar formularios `onsubmit`

## Validando Formularios ##

Ver ejemplos:
  * http://www.webtaller.com/construccion/lenguajes/javascript/lecciones/validar_formularios_en_javascript.php
  * http://www.desarrolloweb.com/articulos/1767.php
  * http://www.tierradenomadas.com/rc011.phtml