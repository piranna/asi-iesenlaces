# Ejercicios #

### Ej 1 ###
Completa las condiciones de los if del siguiente script para que los mensajes de los alert() se muestren siempre de forma correcta:

```
var numero1 = 5;
var numero2 = 8;
 
if(...) {
  alert("numero1 no es mayor que numero2");
}
if(...) {
  alert("numero2 es positivo");
}
if(...) {
  alert("numero1 es negativo o distinto de cero");
}
if(...) {
  alert("Incrementar en 1 unidad el valor de numero1 no lo hace mayor o igual que numero2");
}
```

### Ej 2 ###
El cálculo de la letra del Documento Nacional de Identidad (DNI) es un proceso matemático sencillo que se basa en obtener el resto de la división entera del número de DNI y el número 23. A partir del resto de la división, se obtiene la letra seleccionándola dentro de un array de letras.

El array de letras es:

var letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T'];

Por tanto si el resto de la división es 0, la letra del DNI es la T y si el resto es 3 la letra es la A. Con estos datos, elaborar un pequeño script que:
  1. Almacene en una variable el número de DNI indicado por el usuario y en otra variable la letra del DNI que se ha indicado. (Pista: si se quiere pedir directamente al usuario que indique su número y su letra, se puede utilizar la función prompt())
  1. En primer lugar (y en una sola instrucción) se debe comprobar si el número es menor que 0 o mayor que 99999999. Si ese es el caso, se muestra un mensaje al usuario indicando que el número proporcionado no es válido y el programa no muestra más mensajes.
  1. Si el número es válido, se calcula la letra que le corresponde según el método explicado anteriormente.
  1. Una vez calculada la letra, se debe comparar con la letra indicada por el usuario. Si no coinciden, se muestra un mensaje al usuario diciéndole que la letra que ha indicado no es correcta. En otro caso, se muestra un mensaje indicando que el número y la letra de DNI son correctos.


### Ej 3 ###
A partir de la página web proporcionada y utilizando las funciones DOM, mostrar por pantalla la siguiente información:

  1. Número de enlaces de la página
  1. Dirección a la que enlaza el penúltimo enlace
  1. Numero de enlaces que enlazan a http://prueba
  1. Número de enlaces del tercer párrafo

Modelo: JavascriptModeloEjerciciox


### Ej 4 ###
Completa el código JavaScript proporcionado para que cuando se pinche sobre el enlace se muestre completo el contenido de texto. Además, el enlace debe dejar de mostrarse después de pulsarlo por primera vez. La acción de pinchar sobre un enlace forma parte de los "Eventos" de JavaScript que se ven en el siguiente capítulo. En este ejercicio, sólo se debe saber que al pinchar sobre el enlace, se ejecuta la función llamada muestra().

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Ejercicio 12 - DOM b�sico y atributos XHTML</title>

<style type="text/css">
.oculto { display: none; }
.visible { display: inline; }
</style>

<script type="text/javascript">
function muestra() {

}
</script>
</head>

<body>

<p id="texto">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed mattis enim vitae orci. Phasellus libero. Maecenas nisl arcu, consequat congue, commodo nec, commodo ultricies, turpis. Quisque sapien nunc, posuere vitae, rutrum et, luctus at, pede. Pellentesque massa ante, ornare id, aliquam vitae, ultrices porttitor, pede. <span id="adicional" class="oculto">Nullam sit amet nisl elementum elit convallis malesuada. Phasellus magna sem, semper quis, faucibus ut, rhoncus non, mi. Duis pellentesque, felis eu adipiscing ullamcorper, odio urna consequat arcu, at posuere ante quam non dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis scelerisque. Donec lacus neque, vehicula in, eleifend vitae, venenatis ac, felis. Donec arcu. Nam sed tortor nec ipsum aliquam ullamcorper. Duis accumsan metus eu urna. Aenean vitae enim. Integer lacus. Vestibulum venenatis erat eu odio. Praesent id metus.</span></p>

<a id="enlace" href="#" onclick="muestra(); return false;">Seguir leyendo</a>

</body>
</html>
```

### Ej 5 ###
Completa el código JavaScript proporcionado para que se añadan nuevos elementos a la lista cada vez que se pulsa sobre el botón. Utilizar las funciones DOM para crear nuevos nodos y añadirlos a la lista existente. Al igual que sucede en el ejercicio anterior, la acción de pinchar sobre un botón forma parte de los "Eventos" de JavaScript que se ven en el siguiente capítulo. En este ejercicio, sólo se debe saber que al pinchar sobre el botón, se ejecuta la función llamada añade().
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Ejercicio - DOM básico y atributos XHTML</title>
<script type="text/javascript">
function anade() {
}
</script>
</head>
<body>
<ul id="lista">
	<li>Lorem ipsum dolor sit amet</li>

	<li>Consectetuer adipiscing elit</li>
	<li>Sed mattis enim vitae orci</li>
	<li>Phasellus libero</li>
	<li>Maecenas nisl arcu</li>
</ul>
<input type="button" value="Añadir elemento" onclick="anade();">
</body>
</html>
```