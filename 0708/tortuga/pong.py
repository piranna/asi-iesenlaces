# -*- encoding: utf-8 -*-

"""
$Id$

Jugando con xturtle

Recuerda que tienes que tener instalado el módulo de xturtle (no es estándar de Python)
Descárgalo de http://www.rg16.asn-wien.ac.at/~python/xturtle/xturtle.zip y copia xturtle.py en el directorio de tu programa.
"""

from xturtle import *

# variables para la pantalla
ALTO = 400
ANCHO = 600

# Voy a la esquina superior izquierda para empezar a dibujar el cuadrado
# exterior. Levanto el lápiz para no pintar.
up()
goto(-ANCHO/2, ALTO/2)

# Ya puedo bajar el lápiz
down()
for x in range(2): #dibujo cuadrilátero
    fd(ANCHO)
    rt(90)
    fd(ALTO)
    rt(90)

# vuelvo a levantar para que la bola no pinte en sus movimientos
up()
goto(0,0)  # me coloco en el centro para empezar

# forma y color de la bola
shape("circle")
color("red")

# paso que voy a avanzar (modifica para más rápido o lento)
pasox = 5
pasoy = 5

while True:
    x = xcor()
    y = ycor()
    if x > (ANCHO/2) - 5 or x < -(ANCHO/2) +5:
        pasox = - pasox
    if y > (ALTO/2) - 5 or y < -(ALTO/2) +5:
        pasoy = - pasoy
    goto(x+pasox, y+pasoy)

	
