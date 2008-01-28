# -*- encoding: utf-8 -*-

"""
Dibuja círculos aleatorios.
Incio y fin con el ratón.
"""

from graphics import *
import random, time

def main():
    win = GraphWin("Círculos aleatorios", 300, 300)
    text = Text(Point(150, 30), "Clic para iniciar; clic para terminar.")
    text.draw(win)
    win.getMouse()
    text.undraw()
    
    win.clearLastMouse()                #Nuevo
    while win.getLastMouse() == None:   #Nuevo
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)

        radio = random.randrange(3, 40)        
        x = random.randrange(5, 295)
        y = random.randrange(5, 295)
        
        circle = Circle(Point(x,y), radio)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(.05)
        
    win.close()

main()
