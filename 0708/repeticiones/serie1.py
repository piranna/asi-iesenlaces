# -*- coding: cp1252 -*-
"""
$Id$

Serie de 1 a 100 con salto cada 10 números
"""
for x in range(1,101):
    print "%3d" % x,    # reserva 3 espacios por número
    if x % 10 == 0:     # hace un salto cada 10 números
        print
