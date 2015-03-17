# Programación orientada a objetos #

Un sistema complejo se construye con la interacción de objetos más sencillos.


# Programación sencilla de Gráficos #

  * Módulo: http://mcsp.wartburg.edu/zelle/python/graphics.py
  * Módulo modifiado (para los ejemplos de Harrington) http://www.cs.luc.edu/~anh/python/hands-on/examples/graphics.py

  * Documentación: http://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

  * Más ejemplos en : http://asi-iesenlaces.googlecode.com/svn/trunk/0708/graphics/
  * Documentación de Andrew N. Harrington: http://www.cs.luc.edu/~anh/python/hands-on/handsonHtml/handson.html#x1-830002.4

## Instrucciones ##
Crea una carpeta y descarga el archivo `graphics.py`.

## Mi primer programa ##
```
from graphics import *
win = GraphWin()
```
Por defecto crea una ventana de 200 pixels de alto x 200 pixels de ancho (40.000)
El objeto más sencillo es el punto:
```
>>> p = Point(50, 60)
>>> p.getX()
50
>>> p.getY()
60
>>> p.draw(win)
```

## Ejercicio clase ##
```
# -*- coding: cp1252 -*-
from graphics import *
import time
win = GraphWin("Ventana de ejemplo", 400, 200)

# objeto Point
p = Point(50, 60) # coordenadas: x, y
print p.getX()
print p.getY()
p.draw(win)
p1 = Point( 300   , 180)
p1.draw(win)

# objeto Circle
centro = Point(200,100)
circulo = Circle(centro, 30)
circulo.setFill('red')
circulo.draw(win)

# Textos
etiqueta = Text(Point(200, 60), "Circulo rojo")
etiqueta.draw(win)

# Rectángulos
rect = Rectangle(Point(5,5), Point(395,195))
rect.draw(win)

# líneas
linea = Line(Point(5,5), Point(395,195))
linea.draw(win)

# ovalo
oval = Oval(Point(10,10), Point(390, 190))
oval.draw(win)

time.sleep(10) # dejo 5 segundos abierta la ventana
win.close()
```

## tres en raya ##
```
# -*- coding: cp1252 -*-
from graphics import *
win = GraphWin("Tres en raya")
win.setCoords(0.0, 0.0, 3.0, 3.0)
# líneas verticales
Line(Point(1,0), Point(1,3)).draw(win)
Line(Point(2,0), Point(2,3)).draw(win)
# líneas horizontales
Line(Point(0,1), Point(3, 1)).draw(win)
Line(Point(0,2), Point(3, 2)).draw(win)
raw_input()
```

## Eventos ratón ##
```
# -*- coding: cp1252 -*-
from graphics import *
win = GraphWin("Ratón", 400, 400)
t = Text(Point(200, 200), "")
t.draw(win)

while True:
    punto = win.getMouse()
    t.setText("%d:%d" % (punto.getX(), punto.getY()))   
```

## Cuadrados sencillo ##
```
# -*- coding: cp1252 -*-
from graphics import *
import math
win = GraphWin("Tres en raya")
win.setCoords(0.0, 0.0, 3.0, 3.0)
for x in range(3):
    for y in range(3):
        r = Rectangle(Point(x,y), Point(x+1, y+1))
        r.setFill('red')
        r.setOutline('white')
        r.draw(win)
        

while True:
    punto = win.getMouse()
    x, y = punto.getX(), punto.getY()
    x = math.floor(x)
    y = math.floor(y)
    r = Rectangle(Point(x,y), Point(x+1, y+1))
    r.setFill('blue')
    r.setOutline('white')
    r.draw(win)
```