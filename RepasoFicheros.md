# Repasando que es gerundio #

Ejercicios de repaso de ficheros en python

  1. Escribe una función `sumador(fichero)` que, dado el nombre de un fichero te texto que contiene números separados por espacios en blanco, devuelva la suma de dichos números.
  1. Función `muestra(ruta`. Si **ruta** es un directorio, muestra el contenido del directorio. Si es un nombre de archivo, muestra el contenido del archivo en pantalla.
  1. Función que muestra los programas de python del directorio donde se ejecuta. Versión II: incluye los subdirectorios. _Tip: usa la funcion_ `os.path.isdir`
  1. Función que pide una letra al usuario y muestra los ficheros que comienzan con esa letra (no distingue mayúsculas y minúsculas). _Tip: puedes usar la función_ `glob.glob()` o `os.listdir()`
  1. Función que concatenan los archivos `.txt` de un directorio en un nuevo fichero que se llama `total.txt`
  1. Función que pone en minúsculas los nombres de archivos del directorio donde se ejecuta.
  1. Función que `trocea(fichero, tam)` que crea archivos del tamaño indicado en tam. Por ejemplo si tenemos una arhivo grande `dvd.iso` de 4Gb y usuamos el programa `trocea(dvd.iso, 1024**3)` creará 4 archivos de 1Gb: `dvd.iso.1, dvd.iso.2, dvd.iso.3, dvd.iso.4` _Tip: hay que usar lectura y escritura en modo binario: **rb** y **wb**_





## Ayudas ##
  * os.listdir(ruta) --> devuelve los nombres de archivos de una ruta
  * sys.argv[0](0.md) muestra el nombre del programa.