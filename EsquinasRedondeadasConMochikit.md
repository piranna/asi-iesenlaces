# Esquinas redondeadas con MochiKit #

Con Mochikit es fácil crear efectos visuales, por ejemplo fondos con esquinas redondeadas.


## Pasos ##
  * crear un  `.html` que haga la llamada a los archivos javascript (MochiKit y nuestro). Este archivo tendrá el contenido que queremos presentar. Añadiremos alguna etiqueta `class` e `id`.
  * crear un archivo `.css` que tendrá el color del fondo que queremos mostrar redondeado.
  * crear un archivo `.js` con la función que dirá qué párrafos jhay que redondear y con una llamada para que cuando se cargue la página se llame a nuestra función.

## Archivos que vamos a utilizar ##
  * http://asi-iesenlaces.googlecode.com/svn/trunk/0607/html/redondeado.html
  * http://asi-iesenlaces.googlecode.com/svn/trunk/0607/html/redondeado.css
  * http://asi-iesenlaces.googlecode.com/svn/trunk/0607/html/redondeado.js


## Funciones ##
  * `roundClass(etiqueta[, clase[, opciones]])`.  Redondea todos los elementos que coinciden con la etiqueta y clase. Etiqueta y clase pueden ser nulos y seleccionan a todos.
  * `roundElement(elementoId[, opciones])`. Redondea los elementos con el id indicado.

### Opciones por defecto ###
```
    corners 	"all"
    color 	"fromElement"
    bgColor 	"fromParent"
    blend 	true
    border 	false
    compact 	false
```

### Corners ###
En **corners** podemos especificar:
  * all
  * top
  * bottom
  * tl (arriba izquierda)
  * bl (abajo izquierda)
  * tr (arriba derecah)
  * br (abajo derecha)