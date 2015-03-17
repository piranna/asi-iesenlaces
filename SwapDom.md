# Ejercicios con swapDOM #

## introdom.html ##
```
<?xml version="1.0" encoding="utf-8"?>
<!--
  -->

<!DOCTYPE html PUBLIC  "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xml:lang="en" lang="en">
  <head>
    <title>Introducción a Mochikit</title>
    <meta content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="introdom.css" />
    <script type="text/javascript" src="../MochiKit/MochiKit.js" />
    <script type="text/javascript" src="introdom.js" />
  </head>
  <body>
    <h1>Introducción al uso de DOM</h1>
    <br />
	<div id="mensaje">[No hay mensajes]</div>
	<br />
	<a href="#" onclick="muestraMensaje()">Mostrar mensaje</a> ::
	<a href="#" onclick="borraMensaje()">Borra mensaje</a>
  </body>
</html>

```

## introdom.css ##
```
.avisos {
	background: yellow;
	}
```
## introdom.js ##
```
function muestraMensaje(){
	antiguo = getElement('mensaje');
	nuevo = DIV({'id':'mensaje'}, P({'class':'avisos'}, 'email incorrecto.'));
	swapDOM (antiguo, nuevo);
	}

function borraMensaje(){
	antiguo = getElement('mensaje');
	nuevo = DIV({'id':'mensaje'});
	swapDOM (antiguo, nuevo);
}
```