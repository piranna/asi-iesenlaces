# -*- encoding: utf-8 -*-
# $Id$

"""
En una cadena llamada texto disponemos de un texto formado por
varias frases. ¿Con qué orden simple puedes contar el número de frases?
"""

cadena = """Uno\nDos\nTres"""

numero = len(cadena.split('\n')) 

print 'La cadena tiene', numero, 'frases.'