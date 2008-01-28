# -*- encoding: utf-8 -*-

"""
Ejemplo con dos objetos Entry, conversión del tipo y suma.
"""

from graphics import *

def main():
    anchoVentana = 300
    altoVentana = 300
    
    win = GraphWin("Suma", anchoVentana, altoVentana)
    win.setCoords(0,0, anchoVentana, altoVentana)

    instrucciones = Text(Point(anchoVentana/2, 30),
                     "Introduce dos números.\nDespués haz clic con el ratón.")
    instrucciones.draw(win)

    entry1 = Entry(Point(anchoVentana/2, 250),25)
    entry1.setText('0')
    entry1.draw(win)

    Text(Point(anchoVentana/2, 280),'Primer número:').draw(win)                   
    
    entry2 = Entry(Point(anchoVentana/2, 180),25)
    entry2.setText('0')
    entry2.draw(win)

    Text(Point(anchoVentana/2, 210),'Segundo número:').draw(win)
    
    win.getMouse()  # To know the user is finished with the text.

    numStr1 = entry1.getText()
    num1 = int(numStr1)

    numStr2 = entry2.getText()
    num2 = int(numStr2)

    result = "La suma de \n%s\ny\n%s\nes %s." % (num1, num2, num1+num2)
    Text(Point(anchoVentana/2, 110), result).draw(win)                     
    
    instrucciones.setText("Haz clic para terminar.")
    win.getMouse()
    win.close()

main()
