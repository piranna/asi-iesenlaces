# -*- encoding: utf-8 -*-
# $Id$

""" Normaliza espacios en blanco dentro de una cadena de caracteres:
separa las palabras con un solo espacio en blanco.
"""

ejemplo = "Hola          buenos dias,          aventajados   alumnos"

print ' '.join(ejemplo.split())