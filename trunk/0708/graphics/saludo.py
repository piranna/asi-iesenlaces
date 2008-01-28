# -*- encoding: utf-8 -*-

"""
Ejemplo con objetos tipo Entry
Introduce el nombre, haz clic y verás un saludo
"""

from graphics import *

def main():
    anchoVentana = 300
    altoVentana = 300
    infoHeight = 15         
    win = GraphWin("Greeting", anchoVentana, altoVentana)
    win.setCoords(0,0, anchoVentana, altoVentana)

    instrucciones = Text(Point(anchoVentana/2, 40),
                     "Introduce tu nombre.\nHaz clic después con el ratón.")
    instrucciones.draw(win)

    entry1 = Entry(Point(anchoVentana/2, 200),10)
    entry1.draw(win)

    Text(Point(anchoVentana/2, 230),'Nombre:').draw(win) # etiqueta para el Entry
    
    win.getMouse()  # Para saber cuándo ha introducido el texto el usuario
    
    name = entry1.getText() 

    greeting1 = "Hola, %s!" % name
    Text(Point(anchoVentana/3, 150), greeting1).draw(win)
                     
    greeting2 = "Buenos días, %s!" % name
    Text(Point(2*anchoVentana/3, 100), greeting2).draw(win)
    
    instrucciones.setText("Haz clic para terminar.")
    win.getMouse()
    win.close()

main()
