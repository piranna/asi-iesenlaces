# -*- encoding: utf-8 -*-
'''Programa: triangulo.py
Programa interactivo que dibuja un triángulo,
muestra objetos Texto y recibe información con los click del ratón
'''

from graphics import *

def main():
    anchoVentana = 300
    altoVentana = 300
    win = GraphWin('Dibuja un triángulo', anchoVentana, altoVentana)
    win.setCoords(0, 0, anchoVentana, altoVentana) # reestablece las coordenadas
    win.setBackground('yellow')
    message = Text(Point(anchoVentana/2, 20), 'Haz click en tres puntos')
    message.draw(win)

    # toma y dibuja los puntos del triángulo
    p1 = win.getMouse()  # getMouse devuelve el punto donde ha hecho click el usuario
    p1.draw(win)  # dibuja el punto en la ventana
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]  # ya tenemos los tres vértices del triángulo

    # Usa el objeto Polígono (Polygon) para dibujar el triángulo
    triangulo = Polygon(vertices)
    triangulo.setFill('gray')
    triangulo.setOutline('cyan')
    triangulo.setWidth(4)  # width of boundary line
    triangulo.draw(win)

    # Espera otro clic para terminar
    message.setText('Haz clic para terminar.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    win.getMouse()
    win.close()

main()
