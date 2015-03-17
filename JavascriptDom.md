# DOM (Document Object Model) #

  * API orientado a objetos que permite interactuar con el documento html / xhtml
  * Niveles: 0 (feneración anterior de navegadores), 1 (contenido dinámico) y 2 (estilos dinámicos y eventos avanzados)

## Acceso a algunos elementos ##
  * forms (formularios)
  * images (imágenes)
  * links (enlaces)
  * anchors (marcadores)

Se puede acceder por posición o por nombre

` <form name="datosPersonales" ... > `

Javascript:

```
document.forms[0]
document.datosPersonales
document["datosPersonales"]
```

Para saber si un checkbox o radio está marcado, utiliza la propiedad booleana `checked`.

## DOM 1 ##

Representa el documento como un árbol de nodos. Los nodos son de tipo `Node` y hay varios subtipos: `Document`, `DocumentType`, `Element`, `Text`, `Comment`.


API que permite el acceso y cambio del contenido de un documento:

  * Propiedades de los nodos: `nodeType, nodeName, nodeValue`
  * acceso: {{{getElementById(), getElementsByTagName()
  * getAttribute / setAttribute
  * nodeName, nodeValue
  * childNodes, nextSibling, parentNode
document.forms[0]
document.datosPersonales
document["datosPersonales"]
}}}
```