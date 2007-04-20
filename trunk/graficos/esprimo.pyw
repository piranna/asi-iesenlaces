# -*- coding: utf-8 -*-
# $Id$
# Programa que dice si un número es primo utilizando 
#   una interfaz sencilla

from graphics import *
def es_primo(num):
    """
    Devuelve verdadero si un número es primo. Si no devuelve falso
    """
    esPrimo = True
    for divisor in range(2,int(math.sqrt(num))+1):
        if num % divisor == 0:
            esPrimo = False
            break
    return esPrimo


def main():
    win = GraphWin("Números primos", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Dibuja la interfaz
    Text(Point(1,3), "Introduzca número:").draw(win)
    Text(Point(1,1), ":").draw(win)
    entrada = Entry(Point(2,3), 5)
    entrada.setText("0")
    entrada.draw(win)
    salida = Text(Point(2,1),"")
    salida.draw(win)
    boton = Text(Point(1.5,2.0),"¿Es Primo?")
    boton.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # espera el clic del ratón
    win.getMouse()

    # proceso de conversión
    numero = int(entrada.getText())
    
    if es_primo(numero):
        mensaje = "ES PRIMO"
    else:
        mensaje = "NO ES PRIMO"

    # muestra la salida y cambia el botón
    salida.setText(mensaje)
    boton.setText("Salir")

    # espera el clic y cierra la ventana
    win.getMouse()
    win.close()
    
main()
