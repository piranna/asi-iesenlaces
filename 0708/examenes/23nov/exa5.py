# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe un programa que pida un número entre 1 y 10 (ambos incluidos) 
y lo muestre en la pantalla. Si el número no está en ese rango o si 
lo introducido no es un número, volverá a pedir un número correcto.
"""

numero = raw_input("Introduzca un número")


def esBueno(numero):
    """
    esBueno dice si el número es válido o no
    
    Primero comprueba que es un número: todo son dígitos
    Elimina el signo al principio cuando comprueba los dígitos.
    Segundo comprueba la magnitud
    """
    
    if numero[0]=='-' or numero[0]=='+':
        numeroletras = numero[1:]
    else:
        numeroletras = numero

    for x in numeroletras:  # mira dígito a dígito el número
        if x < '0' or x > '9':
            return False
    if int(numero) < 1 or int(numero) > 10:
        return False
    return True

while not esBueno(numero):
    numero = raw_input("Introduzca un número: ")

print numero

    