# -*- encoding: utf-8 -*-

'''
Recordatorio del módulo graphics: 
Basado en ejemplo de http://www.cs.luc.edu/~anh/python/hands-on/handsonHtml/handson.html
''' 


from graphics import * 
 
def main(): 
    anchoVentana = 200  # variable ancho
    altoVentana = 150   # variable alto
    ventana = GraphWin('Ejemplo graphics', anchoVentana, altoVentana) # damos título y dimensiones
    ventana.setCoords(0, 0, anchoVentana, altoVentana) # coordenadas
 
    cabeza = Circle(Point(40,100), 25) # centro y radio del círculo
    cabeza.setFill("yellow") # color
    cabeza.draw(ventana) 
 
    ojo1 = Circle(Point(30, 105), 5) 
    ojo1.setFill('blue') 
    ojo1.draw(ventana) 
 
    ojo2 = Line(Point(45, 105), Point(55, 105)) # set endpoints 
    ojo2.setWidth(3) 
    ojo2.draw(ventana) 
 
    boca = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box 
    boca.setFill("red") 
    boca.draw(ventana) 
 
    mensaje = Text(Point(anchoVentana/2, 20), 'Haz clic para terminar.') 
    mensaje.draw(ventana) 
    ventana.getMouse() 
    ventana.close() 
 
main() 

