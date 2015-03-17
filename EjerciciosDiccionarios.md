# Ejercicios diccionarios #

  1. Escribe un programa que traduzca una fecha en formato numérico de la siguiente forma: 1-1-08 --> 1 de enero de 08. Usa un diccionario con la correspondencia entre números y meses.
  1. Escribe un programa que pida la ruta de un fichero y muestre las palabras que aparecen en el fichero y el número de veces que se repite cada una.
  1. Escribe un programa llamado traductor. Introduciremos una frase en inglés y la "traducirá" al español. Para ello tendrás que introduccir un diccionario de palabras. Si el programa no conoce una palabra puedes hacer que pida el significado de la misma antes de realizar la traducción.
  1. Si tenemos las asignaturas de los ciclos formativos almacenadas de la siguiente forma:
```
ciclos = {'1ASI': ('fprog', 'sist', 'red', 'fol', 'ret'),
          '2ASI': (xxx, xxx, xxx, xxxx),
          ...
modulos = {'fprog': 'Fundamentos de Programación',
           'red': 'Redes de área local',
           'sist': 'Sistemas operativos'
           }
horas = {'fprog': 8,
         'red': 10,
         etc
        }

```
Crea un programa que dada esta estructura pida el nombre de un ciclo y muestre las asignaturas con su nombre completo y el número de horas entre paréntesis:
```
1ASI:     Fundamentos de programación  (8 horas semanales)
          Redes de área local          (10 horas semanales)
```