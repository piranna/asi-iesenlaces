# -*- encoding: utf-8 -*-

'''
Elige los colores de la casa con clics
'''

from graphics import *

def estaEntre(x, end1, end2):
    '''Devuelve True si x está entre los límites: end1 y end2.
    Los límites no tienen por qué estar en orden creciente.'''
    
    return end1 <= x <= end2 or end2 <= x <= end1

def estaDentro(point, rect):
    '''Devuelve True si el punto está dentro del triángulo. '''
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return estaEntre(point.getX(), pt1.getX(), pt2.getX()) and \
           estaEntre(point.getY(), pt1.getY(), pt2.getY())

def creaRectColor(esquina, ancho, alto, color, win):
    ''' Devuelve un rectángulo dibujado en win con la esquina 
    izquierda y el color especificado.'''
    esquina2 = esquina.clone()  
    esquina2.move(ancho, -alto)
    rect = Rectangle(esquina, esquina2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def main():
    anchoVentana = 400
    altoVentana = 400
    win = GraphWin('Selecciona Colores', anchoVentana, altoVentana)
    win.setCoords(0, 0, anchoVentana, altoVentana) # coordenadas

    botonRojo = creaRectColor(Point(310, 350), 80, 30, 'red', win)
    botonAmarillo = creaRectColor(Point(310, 310), 80, 30, 'yellow', win)
    botonAzul = creaRectColor(Point(310, 270), 80, 30, 'blue', win)

    house = creaRectColor(Point(60, 200), 180, 150, 'gray', win)
    door = creaRectColor(Point(90, 150), 40, 100, 'white', win)
    roof = Polygon(Point(50, 200), Point(250, 200), Point(150, 300))
    roof.setFill('black')
    roof.draw(win)
    
    msg = Text(Point(anchoVentana/2, 375),'Elige el color de la casa.')
    msg.draw(win)
    pt = win.getMouse()

    if estaDentro(pt, botonRojo):
        color = 'red'
    elif estaDentro(pt, botonAmarillo):
        color = 'yellow'
    elif estaDentro(pt, botonAzul):
        color = 'blue'
    else :
        color = 'white'
    house.setFill(color)
    
    msg.setText('Elige el color de la puerta.')
    pt = win.getMouse()

    if estaDentro(pt, botonRojo):
        color = 'red'
    elif estaDentro(pt, botonAmarillo):
        color = 'yellow'
    elif estaDentro(pt, botonAzul):
        color = 'blue'
    else :
        color = 'white'
    door.setFill(color)

    msg.setText('Haz clic para terminar.')
    win.getMouse()
    win.close()

main()
