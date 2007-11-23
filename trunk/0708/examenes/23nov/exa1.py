# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe un programa que pida su nombre al usuario. Si el usuario escribe 
el nombre en mayúsculas, el programa lo imprime en pantalla en minúsculas 
y al revés.
""


nombre = raw_input("Introduzca su nombre: ")

nuevo = "" # nuevo nombre
for letra in nombre:
    if letra.isupper():  #letra >='A' and letra <= 'Z'
        nuevo += letra.lower()
    else:
        nuevo += letra.upper()
print nombre, 'con las letras cambiadas es', nuevo