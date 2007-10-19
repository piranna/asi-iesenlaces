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
ht()
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
t1 = Pen()
t2 = Pen()
t1.shape("circle")
t2.shape("circle")
t2.color("blue")
t1.color("red")
t1.up()
t2.up()

# paso que voy a avanzar (modifica para más rápido o lento)
pasox = 3
pasoy = 3
pasx = 3.5
pasy = 3.5
while True:
    x = t1.xcor()
    y = t1.ycor()
    if x > (ANCHO/2) - 5 or x < -(ANCHO/2) +5:
        pasox = - pasox
    if y > (ALTO/2) - 5 or y < -(ALTO/2) +5:
        pasoy = - pasoy
    t1.goto(x+pasox, y+pasoy)
    
    x = t2.xcor()
    y = t2.ycor()
    if x > (ANCHO/2) - 5 or x < -(ANCHO/2) +5:
        pasx = - pasx
    if y > (ALTO/2) - 5 or y < -(ALTO/2) +5:
        pasy = - pasy
    t2.goto(x+pasx, y+pasy)
	
