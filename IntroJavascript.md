` Basado en materiales de Simon Willison - http://simonwillison.net/ `


## Introducción ##
Javascript fue creado por Brendan Eich (Netscape) en 1995. Se llamó inicialmente LiveScript y aparece con Netscape 2.

Microsoft lanzó JScript con IE 3.

Netscape envió el lenguaje a Ecma International: en 1997 nace Ecmascript.

No tiene un concepto de entrada y salida y se diseñó para funcionar como lenguaje de script en un cliente. Hoy podemos encontrar js no sólo en los navegadores, sino también en  Adobe Acrobat, Photoshop, Yahoo!'s Widget engine y más.

## Dónde ##
**En el encabezado**
```
<html>
  <head>
    <script type="text/javascript">
       ...
    </script>
  </head>
<body>
</body>
</html>
```

**En un fichero aparte**
```
<html>
<body>
  <script src="externo.js" type="text/JavaScript"></script>
  <noscript>
      Esto sólo se muestra si el navegador tiene javascript desactivado.
  </noscript>
</body>
</html>
```

## Tipos de datos ##

Los programas js manipulan valores y esos valores pertenecen a un tipo. Los tipos en js pueden ser:

  * Números
  * Strings
  * Booleanos
  * Objetos
    * Funciones
    * Arrays
    * Fechas
    * RegExp
  * Null
  * Undefined

También hay unos tipos Indefinido y Null. Los Arrays son un tipo especial de objeto. También hay Fechas y Expresiones regulares. Las funciones también son un tipo especial de objeto.

### Números ###

Soporta los opereadores stándar. Hay un objeto (Math) que gestiona las operaciones avanzadas.
```
4 * 5 = 20;
Math.sin(3.5);
d = Math.PI * r * r;
```
#### Conversiones ####
```
> parseInt("123")
123
> parseInt("010")
8
> parseInt("123", 10)
123
> parseInt("010", 10)
10
```


JavaScript tiene también un valor especial llamado `Not-a-Number`
```
> parseInt("hello", 10)
NaN
> NaN + 5
NaN
> isNaN(NaN)
true
```

Valores de Intinito:
```
> 1 / 0
Infinity
> -1 / 0
-Infinity
```

### Cadenas (Strings) ###

Las cadenas son secuencias de caracteres unicode. Un carácter es una cadena de longitud 1.
```
> "hola".length
4
> "hola".charAt(0)
h
> "hola, mundo".replace("hola", "adiós")
adiós, mundo
> "hola".toUpperCase()
HOLA
```
### Otros tipos ###

`Null`  y `Undefined`.

#### booleanos ####
operadores `&&, , ! `

## Variables ##

Declaración de nuevas variables:
```
var a;
var name = "simon";
```
El valor de una variable está indefinido hasta que se le asigna un valor.


## Operadores ##

Operadores numéricos `+, -, *, / y %`
También `x += 5 x = x + 5 `

El operador `+` también concatena cadenas:
```
> "hello" + " world"
hello world
```
```
> "3" + 4 + 5
345
> 3 + 4 + "5"
75
```

### Comparaciones ###
`<, >, <= y >=`
Se pueden usar para cadenas y números.

## Estructuras de control ##
```
var name = "???";
var numAlumnos ;
if (curso == "asi") {
  numAlumnos = 25;
} else if (curso == "dai") {
  numAlumnos = 15;
} else {
  numAlumnos = 30;
}
```

```
while (true) {
  // an infinite loop!
}

```

```
do {
  var input = get_input();
} while (inputIsNotValid(input))
```


```
for (var i = 0; i < 5; i++) {
  // ejecuta 5 veces;
}

```

```
var allowed = (age > 18) ? "yes" : "no"; 
```

```
switch(action) {
    case 'draw':
        drawit();
        break;
    case 'eat':
        eatit();
        break;
    default:
        donothing();
}
```

## Objetos ##
Los objetos son colecciones de pares nombre-valor (como los diccionarios de Python)

```
var obj = new Object();
var obj = {};
```
Son semánticamente equivalentes.
```
obj.nombre = "Simon"
var nombre = obj.nombre;

obj["nombre"] = "Simon";
var nombre = obj["nombre"];
```


## Arrays ##
```
> var a = new Array();
> a[0] = "perro";
> a[1] = "gato";
> a[2] = "gallina";
> a.length
3

> var a = ["perro", "gato", "gallina"];
> a.length
3
```

```
for (var i = 0; i < a.length; i++) {
    // Haz algo con a[i]
}
```

o mejor

```
for (var i = 0, j = a.length; i < j; i++) {
    // Do something with a[i]
}

```

#### métodos ####
```
a.toString(), a.toLocaleString(), a.concat(item, ..), a.join(sep),
a.pop(), a.push(item, ..), a.reverse(), a.shift(), a.slice(start, end),
a.sort(cmpfn), a.splice(start, delcount, [item]..), a.unshift([item]..)
```

## Funciones ##
```
function suma(x, y) {
    var total = x + y;
    return total;
}
```

Puede tomar 0 o más parámetros. Si no hay un `return`, devuelve un valor indefinido.

```
function add() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum;
}
```
```
> add(2, 3, 4, 5)
14
```
Otro ejemplo:
```
function avg() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum / arguments.length;
}
> avg(2, 3, 4, 5)
3.5
```

Media de vector:
```
function avgArray(arr) {
    var sum = 0;
    for (var i = 0, j = arr.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum / arr.length;
}
> avgArray([2, 3, 4, 5])
3.5
```


## Más Objetos ##

```
function makePerson(first, last) {
    return {
        first: first,
        last: last
    }
}
function personFullName(person) {
    return person.first + ' ' + person.last;
}
function personFullNameReversed(person) {
    return person.last + ', ' + person.first
}
> s = makePerson("Simon", "Willison");
> personFullName(s)
Simon Willison
> personFullNameReversed(s)
Willison, Simon
```

Más fácil:
```
function makePerson(first, last) {
    return {
        first: first,
        last: last,
        fullName: function() {
            return this.first + ' ' + this.last;
        },
        fullNameReversed: function() {
            return this.last + ', ' + this.first;
        }
    }
}
> s = makePerson("Simon", "Willison")
> s.fullName()
Simon Willison
> s.fullNameReversed()
Willison, Simon
```