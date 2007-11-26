# -*- encoding: utf-8 -*-
# $Id$

ciclistas = ['Pere Porcar', 'Joan Beltran', 'Lledó Fabra']

tiempo = [[10092.0, 12473.1, 13732.3, 10232.1, 10332.3],
          [11726.2, 11161.2, 12272.1, 11292.0, 12534.0],
          [10193.4, 10292.1, 11712.9, 10133.4, 11632.0]]

def ganador (nombres, tiempos):
    suma_tiempos = []
    for tiempos_corredor in tiempos:
        suma_tiempos.append(sum(tiempos_corredor))
    # ahora tenemos en suma_tiempos la suma de cada corredor
    # vamos a averiguar a quién corresponde
    mejor = 0  # en mejor almacenaremos la posición del mejor tiempo
    tiempo_mejor = suma_tiempos[0]
    for c in range(1, len(suma_tiempos)):  # el primero (#0) ya lo hemos leído
        if suma_tiempos[c] < tiempo_mejor:
            mejor = c
            tiempo_mejor = suma_tiempos[c]
    # en mejor tenemos el índice del ciclista que tiene mejor tiempo
    # devolvemos su nombre
    return nombres[mejor]
    
    
print ganador(ciclistas, tiempo)
