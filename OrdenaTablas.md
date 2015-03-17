# Ordenar tablas #

En las demos de mochikit hay un ejemplo de ordenar tablas (http://mochikit.com/examples/sortable_tables/index.html) Vamos a ver cómo podemos utilizar el fuente javascript que usan para crear nuestras propias tablas (http://mochikit.com/examples/sortable_tables/sortable_tables.js)

No vamos a reinventar la rueda y vamos a utilizar un código que ya funciona, adaptándolo a nuestras necesidades.

## ¿Cómo funciona el programa? ##

Básicamente **cuando se carga la página** el `SortableManager`:

  * Busca la tabla por su id: tablaordenable.
  * Analiza sus thead con atributos "mochi:formato"
  * Analiza los datos fuera del tbody basándose en la información obtenida y clona los elementos tr para usarlos más tarde.
  * Clona los th de las columnas
  * Almacena una referencia al tbody, que se reemplazará en cada ordenación
  * Realiza la primera ordenación.

**Cuando se pide una ordenación**:

  * Ordena los datos basándose en la clave y dirección
  * Crea un nuevo tbody con las filas de la nueva ordenación
  * Reemplaza el encabezado los encabezados con versiones cliclables, añadiendo un indicador a la última columna ordenada

## ¿Cómo hacer que se pueda ordenar una tabla en nuestro .html? ##
  * Incluir el programa .js que ordena las tablas (genérico). Nosotros lo hemos llamado tablas.js
  * En el html añadir a la tabla que queremos ordenar el atributo `id="sortable_table`.
  * Los `th` del `thead` de la tabla deberán indicar el tipo de dato que contiene cada columna para aplicarle la función de ordenación apropiada. Lo haremos con un atributo (no esándard) `mochi:format="valor"`. En nuestro ejemplo:
```
<th mochi:format="str">Alumno</th>
<th mochi:format="str">Curso</th>
<th mochi:format="fecha">Fecha Nac</th>
<th mochi:format="numero">Nota</th>
```
  * En el archivo .js tendremos que añadir a `SortableManager` las funciones apropiadas para que javascript sepa qué tipo de dato tiene que ordenar, ya que en el html todo es texto. En nuestro caso quedará así:
```
             switch (this.columns[j].format) {
                    case 'isodate':
                        obj = isoDate(obj);
                        break;
                    case 'str':
                        break;
                    case 'istr':
                        obj = obj.toLowerCase();
                        break;
                    // cases for numbers, etc. could be here
		    // añadimos funciones para nuestras columnas
		    case 'numero':
			obj = eval(obj);
			break;
		    case 'fecha':
			obj = convierteFecha(obj);
			break;
                    default:
                        break;
                }

```

**convierteFecha** es una función que hemos creado nosotros para que tome la fecha de forma correcta.

## Fuentes del ejemplo ##
  * http://asi-iesenlaces.googlecode.com/svn/trunk/html/tablas.html
  * http://asi-iesenlaces.googlecode.com/svn/trunk/html/tablas.css
  * http://asi-iesenlaces.googlecode.com/svn/trunk/html/tablas.js