# -*- coding: cp1252 -*-

# Ejemplo funciones recursivas

def factorial(n):
	"""factorial del número 5 --> 5*4*3*2*1
"""
	resultado = 5
	for i in range(1,n):
		resultado *= i  # resultado = resultado * i
	return resultado

def potencia(x,n):
	if  n == 0:
		return 1
	else:
		return x * potencia(x, n-1)
