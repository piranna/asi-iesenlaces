# Introducción al entorno #

## Documentación ##
  * http://www.lcc.uma.es/~pedre/LP_DevC.htm

## Opciones interesantes ##
  1. Herramientas -> Opciones del compilador -> Configuración -> Linker -> Generar información de debug -> YES
  1. Herramientas -> Opciones del entorno -> Principal: Activar Crear archivo de respaldo
  1. Herramientas -> Opciones del editor -> Principal: Activar Resaltar llaves y parentesis concordantes.
  1. Herramientas -> Opciones del editor -> Visualización: Activar Número de línea.
  1. Herramientas -> Opciones del editor -> Sintaxis: Seleccionar en Pre-configuracicones: Classic

## Código por defecto ##

**Herramientas --> Opciones del editor --> Código --> Código por defecto**

```
/*----------------------------------------------------------------
|  Autor:                                                         |
|  Fecha:                               Versión: 1.0              |
|-----------------------------------------------------------------|
|  Descripción del Programa:                                      |
|                                                                 |
| ----------------------------------------------------------------*/

// Incluir E/S y Librerías Standard
#include <stdio.h>
#include <stdlib.h>

// Zona de Declaración de Constantes

// Zona de Declaración de Tipos

// Zona de Cabeceras de Procedimientos y Funciones

// Programa Principal
int main()
{
    // Zona de Declaración de Variables del Programa principal

    system("Pause");    // Hacer una pausa
    return 0;           // Valor de retorno al S.O.
}

// Implementación de Procedimientos y Funciones
```
## Documentación en línea ##
  * Descargar el manual de la biblioteca estándar de C para Dev-C++ 5 (1,29 MB).
  * Abrir el Manejador de Paquetes de Dev-C++ (Herramientas -> Package Manager).
  * Pulsar Install y seleccionar GlibcHelp.DevPak
  * Seleccionar Ayuda -> Configurar el Menú de ayuda
    1. Pulsar Añadir y seleccionar Libc.hlp (posiblemente en C:\Dev-Cpp\Help).
    1. Editar el texto del menú para que ponga "Manual de Ayuda de la biblioteca estándar de C"
    1. Activar Busca en el archivo...