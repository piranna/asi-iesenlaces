# -*- coding: cp1252 -*-
# cuenta las letras de un fichero de texto
import pprint  # para imprimir el diccionario

def cuentaLetras(fichero):
    """Abro el fichero y leo letra a letra
"""
    # abrir el fichero para lectura
    f = open(fichero)

    # crear variables
    letras = {}  # diccionario vacío

    # procesar fichero letra a letra
    letra = f.read(1)
    while letra:
        if letra.isalpha():
            letra = letra.lower()  # conversión a minúsculas
            letras[letra] = letras.get(letra,0) + 1  # Incrementamos su valor: si no existía, pondrá 1
        letra = f.read(1)
    f.close()
    return letras

def cuentaLetras2(fichero):
    """Leo el fichero entero y proceso letra a letra
"""
    # abrir el fichero para lectura
    f = open(fichero)

    # crear variables
    letras = {}  # diccionario vacío

    # procesar fichero letra a letra
    contenido = f.read()
    for letra in contenido:
        if letra.isalpha():
            letra = letra.lower()  # conversión a minúsculas
            letras[letra] = letras.get(letra,0) + 1  # Incrementamos su valor: si no existía, pondrá 1
    f.close()
    return letras

def cuentaPalabras(fichero):
    """Leo el fichero entero y proceso letra a letra
"""
    # abrir el fichero para lectura
    f = open(fichero)

    # crear variables
    palabras = {}  # diccionario vacío

    # procesar fichero letra a letra
    contenido = f.read()
    listaPalabras = contenido.split(' ')
    for palabra in listaPalabras:
        if palabra.isalpha():
            palabras[palabra] = palabras.get(palabra, 0) +1
    f.close()
    return palabras

def masUsada(dicc):
    """ dicc: parejas--> letra:repeticiones
"""
    repeticiones = dicc.values()
    repeticiones.sort()
    for k in dicc.keys():
        if dicc[k] == repeticiones[-1]:
            print 'Letra más usada', k
        

# utilizo primera función
letras = cuentaLetras('muestraletras.py')
# mostrar resultado
pprint.pprint(letras)
print '*' * 40
# utilizo segunda función
letras = cuentaLetras2('muestraletras.py')
# mostrar resultado
pprint.pprint(letras)
print '*' * 40
# utilizo función cuentaPalabras
palabras = cuentaPalabras('muestraletras.py')
pprint.pprint(palabras)
