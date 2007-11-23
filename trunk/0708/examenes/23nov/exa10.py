# -*- encoding: utf-8 -*-
# $Id$

"""
Escribe una función que reciba una lista de nombres y que imprima la 
lista ordenada. La lista tendrá la siguiente estructura: 
[ “Ana, Martínez, Blasco”, “Nombre,Apellido1, Apellido2”, ...]. 
La ordenación se hará según el siguiente criterio: 
Apellido1 – apellido2 – Nombre. Es decir, se ordena por el primer 
apellido, si coincide, se ordena por el segundo apellido y si coincide 
también, se ordena por el nombre. El listado se hará de forma tabulada 
dejando 15 espacios para cada elemento.
"""
def esMayor(nombre1, nombre2):
        """
        nombre tiene la estructura "Nombre, Apellido1, Apellido2" por eso 
        hacemos un split(',') para separar la información
        Un nombre es mayor, cuando el primer apellido es mayor. Si no se compara
        el segundo apellido y en última instancia el nombre
        """
        nom1, ape1_1, ape1_2 = nombre1.split(',')
        nom2, ape2_1, ape2_2 = nombre2.split(',')
        if ape1_1 > ape2_1:
                return True
        elif ape1_1 == ape2_1:
                if ape1_2 > ape2_2:
                        return True
                elif ape1_2 == ape2_2:
                        if nom1 > nom2:
                                return True
        return False

        

def ordenaListaNombres(lNombres):
        """
        compara apellido1, apellido2 y nombre
        """
        for x in range(1, len(lNombres)):
                for y in range(len(lNombres)-x):
                        if esMayor(lNombres[y], lNombres[y+1]):
                                lNombres[y], lNombres[y+1] = lNombres[y+1], lNombres[y]
                                
lista = ["Ana, Marco, Perez", "Pablo, Marco, Jimenez","Ana, Marco, Jimenez"]

ordenaListaNombres(lista)

print lista