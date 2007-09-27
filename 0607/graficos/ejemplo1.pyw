# -*- coding: utf-8 -*-
## Author: oldham@centre.edu
## Adaptado por lm

from graphics import *

win = GraphWin( "Ejemplo de gráficos", 350, 450 )

t1 = Text(Point(50, 20), "Círculos:")
t1.draw(win)

c1 = Circle(Point( 100, 20 ), 10 )
c1.draw(win)

c2 = Circle( Point( 200, 20 ), 20 )
c2.setWidth(4)
c2.setFill( "blue" )
c2.draw(win)

c3 = Circle( Point( 300, 20 ), 10 )
c3.setWidth(0)
c3.setFill( "red" )
c3.draw(win)

t1 = Text( Point(50, 80 ), "Líneas:")
t1.draw( win )

ln = Line( Point(100,80), Point(300, 120) )
ln.setWidth(5)
ln.draw(win)

ln = Line( Point(100, 120), Point(300, 80) )
ln.setWidth(2)
ln.setFill("blue")
ln.draw(win)

Text( Point( 50, 180 ), "Rectángulos\n&Elipses" ).draw(win)

Rectangle( Point( 100, 180 ), Point( 200, 250 ) ).draw(win)
Oval( Point(100,180), Point(200,250) ).draw(win)

Text( Point( 50, 275 ), "Polígonos" ).draw(win)
pts = [ Point( 100, 275 ), Point( 250, 300 ), Point( 150, 425 )]
Polygon( pts ).draw(win)

# Para finalizar
win.getMouse()








