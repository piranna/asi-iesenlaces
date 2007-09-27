# -*- coding: utf-8 -*-
# convert_gui.pyw
# Programa que convierte de Celsius a Fahrenheit utilizando 
#   una interfaz sencilla

from graphics import *

def main():
    win = GraphWin("Convertidor de Celsius a Fahrenheit", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Dibuja la interfaz
    Text(Point(1,3), "   Temperatura en Celsius:").draw(win)
    Text(Point(1,1), "Temperature en Fahrenheit:").draw(win)
    entrada = Entry(Point(2,3), 5)
    entrada.setText("0.0")
    entrada.draw(win)
    salida = Text(Point(2,1),"")
    salida.draw(win)
    boton = Text(Point(1.5,2.0),"Convertir")
    boton.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # espera el clic del ratón
    win.getMouse()

    # proceso de conversión
    celsius = eval(entrada.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    # muestra la salida y cambia el botón
    salida.setText("%0.1f" % fahrenheit)
    boton.setText("Salir")

    # espera el clic y cierra la ventana
    win.getMouse()
    win.close()
    
main()
