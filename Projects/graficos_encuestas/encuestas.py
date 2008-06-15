#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
(c) lm 2008
GPL licensed

Planteamiento del problema
==========================
* Los resultados de las encuestas están en una hoja de cálculo excell.
* Hay que hacer unos gráficos con la información de las encuestas para
  enviar a los departamentos.
* Se organizarán los gráficos por encuestas (de la 4 a la 23) (las 3 primeras no)
* Cada encuesta recogerá información de la media del módulo, la desviación
  típica, la media del curso y la media del departamento.

Propuesta de solución
=====================
* Transformar la hoja de xls a csv
* Procesar el csv para extraer la información
* Generar los gráficos con matplotlib.plot()


v.082b
"""

import csv
import sys
from pylab import *
from numpy import average, std



departamentos = {}
import shelve

def lee_csv():
    """
	Lee fichero csv y devuelve lista de líneas leídas
	"""
    reader = csv.reader(open('datos.csv'))
    lineas = [row for row in reader]
    return lineas


def crear_estructura(lineas):
    """
    a partir de la lista de líneas del fichero csv:
    creo estructura de datos para almacenar las encuestas:
    árbol de diccionarios  departamentos  -> grupos --> módulos --> encuestas:valores
    --> devuelve departamentos
    """
    departamentos = {}
    for d in lineas[0][3:]:
        departamentos[d]= {}	
    for n, g in enumerate(lineas[1][3:]):
        departamentos[lineas[0][n+3]][g]={}
    for n, m in enumerate(lineas[2][3:]):
        departamentos[lineas[0][n+3]][lineas[1][n+3]][m] = {}
    for d in departamentos:
        for g in departamentos[d]:
            for m in departamentos[d][g]:
                for x in range(1, 24):
                    departamentos[d][g][m][str(x)]= {}
    return departamentos

def introduce_info(departamentos, lineas):
    """
    Introduce la información del fichero csv (lista de líneas) en
    la estructura creada (departamentos)

    La información de los departamentos está en la primera línea
    (a partir de la tercera columna)
    Cada departamento tiene debajo sus grupos (línea 2)
    Cada grupo tiene debajo sus módulos (línea 3)
    """
    deps = lineas[0][3:]
    grupos = lineas[1][3:]
    modulos = lineas[2][3:]

    enc = "1" # número de encuesta
    for l in lineas[3:]:
        if l[1] != '':
            enc = l[1]
        for col in range(96-3):
            departamentos[deps[col]][grupos[col]][modulos[col]][enc][l[2]] = l[col+3]


def resumen_datos(departamentos):
    """
    Genera el resumen de datos para generar los gráficos.
    De las 23 encuestas, procesa sólo las 20 con tratamiento numérico:
    de la 4 a la 24.
    Crea una lista de diccionarios. Cada posición de la lista corresponde
    a una encuesta. La posición 0 corresponde a la primera tratada (la 4) y 
    la posición 19 a la última (la 23)
    """
    # preparo estructura:lista de 20 diccionarios
    resumen = []
    for x in range(20):
        resumen.append({})

    # procesado de encuestas:
    for i in range(20):   # tratamos 20 encuestas: de la 4 a la 23
        for d in departamentos:
            datosDep = []
            for g in departamentos[d]:
                datosGrupo = []
                for m in departamentos[d][g]:
                    datosMod = []
                    #print departamentos[d][g][m]
                    datosEnc = departamentos[d][g][m][str(i+4)]   # la encuesta estaba como str
                    for resp in datosEnc:
                        if resp.isdigit():  #descarto NS/NC
                            numResp = int(resp)
                            dato = datosEnc[resp]
                            if dato.isdigit():
                                datosMod += [numResp]*int(dato) # Añado las veces que se repite la respuesta
                    # Cuidado hay módulos que se repiten en distintos grupos.
                    # Tengo que añadirle el nombre del grupo para distinguirlos.
                    resumen[i][m+'::'+g]= {}
                    resumen[i][m+'::'+g]['media'] = average(datosMod)
                    resumen[i][m+'::'+g]['des'] = std(datosMod)
                    datosGrupo += datosMod
                # trato grupo
                resumen[i][g] = average(datosGrupo)
                datosDep += datosGrupo
            # trato dept
            resumen[i][d] = average(datosDep)

    return resumen



def titulo(n):
    """
    titulo(numero)
    Devuelve el título de una encuesta.
    No lo uso en la versión actual.
    """
    titulos = """1.- ¿ Informa de los objetivos, contenidos y materiales recomendados?
2.- ¿ Informa de los criterios de evaluación y calificación?
3.- ¿ Informa de las pruebas y actividades para la evaluación?
4.- Explica de manera clara y ordenada
5.- Destaca los aspectos fundamentales de cada tema y actividad
6.- Relaciona  la parte teórica  con su aplicación práctica.
7.- Fomenta la participación de los alumnos
8.- Hace interesantes las clases
9.- Utiliza la  pizarra, transparencias, videos, CD´s, internet, etc. que te ayudan  a comprender los temas
10.- Califica de forma clara y objetiva
11.- Exige en los exámenes  y trabajos de acuerdo a lo impartido y lo trabajado en clase
12.- Permite revisar y comentar los exámenes.
13.- Comienza las clase a la hora fijada
14.- Es correcto y respetuoso con los alumnos
15.- Tiene un trato igualitario con todos los alumnos
16.- Responde con interés a las intervenciones de los alumnos
17.- La labor docente de este profesor me parece
18.- Me siento satisfecho con lo aprendido en este módulo
19.- La relación de este profesor con los alumnos me parece
20.- Considero mi preparación previa suficiente para seguir este módulo
21.- Llevo al día el estudio de este módulo
22.- Resuelvo las dudas preguntando en clase
23.- Tengo actitud activa en clase, atiendo, participo"""

    titulos = titulos.split('\n')
    return titulos(n)


def grafico(enc, datos, datosgrupo, etiquetas_x, tit):
    """
    Genera grafico de barras. 

    Primer test. No se esta usando.
    """
    N = len(datos)
    #menMeans = (20, 35, 30, 35, 27)
    #menStd =   ( 2,  3,  4,  1,  2)
    ind = arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    p1 = bar(ind, datos, width, color='r') #, yerr=menStd)

    #womenMeans = (25, 32, 34, 20, 25)
    #womenStd =   ( 3,  5,  2,  3,  3)
    p2 = bar(ind+width, datosgrupo, width, color='y') #, yerr=womenStd)

    ylabel('Respuestas')
    title(unicode(tit, 'utf-8'))
    xticks(ind+width, etiquetas_x)
    xlim(-width,len(ind))
    total = max(max(datosgrupo), max(datos))

    yticks(arange(0,total+2))

    legend( (p1[0], p2[0]), (enc, 'Media grupo' ), shadow=True)
    show()

    savefig(enc.replace('/', '_') + '.png')
    clf()

    #grafico('ostt_1', [9,0], [8,2], ('Si', 'No'), 'Grafico de esto')

def dame_media_grupo(grupo, enc, n):
    """
    Genera media de un grupo para una encuesta que tiene n preguntas
    No lo estamos usando.
    """
    resultado = [0] * n
    for m in grupo.keys():
        claves = grupo[m][enc].keys()
        claves.sort()
        for n, res in enumerate(claves):
            resultado[n] += int(grupo[m][enc][res])
    num = len(grupo.keys())*1.0
    resultado = [r/num for r in resultado]
    return resultado


def grafico_barras():
    """
    Test para grafico de barras.
    No se está usando.
    """
    for dep in departamentos.keys():
        for g in departamentos[dep]: # miro los grupos de cada dep
            for m in departamentos[dep][g]: # miro los módulos de cada módulo
                for enc in range(len(departamentos[dep][g][m].keys())):
                    claves = departamentos[dep][g][m][str(enc+1)].keys()
                    claves.sort()   # MUY importante: orden de las claves
                    datos = []
                    for k in claves:
                        datos.append(int(departamentos[dep][g][m][str(enc+1)][k]))
                    grafico(str(enc+1)+'_'+m, 
                            datos, 
                            dame_media_grupo(departamentos[dep][g], str(enc+1), len(claves)),
                            sorted(departamentos[dep][g][m][str(enc+1)].keys()), 
                            titulos[enc])


def dibujaLinea(modulo, departamento, grupo, media_mod, desv_mod, dat_grupo, dat_depto):
    """
    Genera gráfico de líneas con los siguientes datos:
    modulo: nombre del módulo
    departamento: nombre del departamento
    grupo: nombre del grupo
    media_mod: lista de datos con la media de datos del grupo para las 20 encuestas.
    desv_mod: lista con la desviación típica para las 20 en.
    dat_grupo: media del grupo en las 20 enc.
    dat_depto: media del depto en las 20 enc.
    Se guarda el archivo con el nombre: modulo_grupo.png
    El nombre del modulo se ha transformado. Se ha cambiado '/' por '_' porque no es un
    carácter válido para nombres de archivos.
    """
    clf()
    t = arange(4, 24, 1)
    
    print 'Generando gráfico de', modulo, '[',grupo,']'
    #print media_mod
    #print '*' * 5 , len(media_mod)
    
    plot(t, media_mod,'-o', t, desv_mod, 'r-v', t, dat_grupo, ':^', t, dat_depto, ':s')

    legend(('Media', 'Desv', 'Grupo', 'Depto'), loc = 'upper right', shadow=True)
    # Arreglo nombre de módulo
    nom_modulo = modulo.split('/')[0].strip()
    title(u'Módulo: %s [%s :: %s]' % (unicode(nom_modulo, 'utf-8'), 
                                     unicode(grupo, 'utf-8'), 
                                     unicode(departamento, 'utf-8')))
    # GRID 
    #Dibuja las líneas verticales del grid
    grid(True)    
    for p in range(4, 24):
        axvline(x = p, c='g', ls=':')
    # límites del grid
    xlim(2,25)
    ylim(0,6)
    #ylabel(u'Núm. Respuestas')
    xlabel(u'Núm. Pregunta')
    
    draw()
    # guarda: atención con el nombre del archivo: hay módulos que se repiten en distintos grupos.
    savefig(modulo.replace('/', '_')+'_'+grupo+'.png')

def hazmeGraficos(departamentos, resumen):
    for dep in departamentos.keys():
        for g in departamentos[dep]: # miro los grupos de cada dep
            #raw_input('--> ')
            for m in departamentos[dep][g]:
                # recopilacion de datos:
                modulo = []
                desviacion = []
                grupo = []
                depto = []
                for p in range(20):
                    ## Recordad que distingo el módulo con m+'::'+g
                    modulo.append(resumen[p][m+'::'+g]['media'])
                    desviacion.append(resumen[p][m+'::'+g]['des'])
                    grupo.append(resumen[p][g])
                    depto.append(resumen[p][dep])
                dibujaLinea(m, dep, g, modulo, desviacion, grupo, depto)



def creaHtmls(departamentos):
    for dep in departamentos.keys():
        f = open(dep+'.html', 'w')
    plantilla = """<?xml version="1.0" encoding="utf-8" ?>
    <!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
<title>%s</title>
<link rel="text/stylesheet" href="estilos.css" />
</head>
<body>"""
    f.write(plantilla % dep)
    # titulo
    f.write("\n<h1>%s</h1>\n" % dep)
    f.write("<h3>Indice</h3>\n")
    for g in sorted(departamentos[dep].keys()):
        f.write('<a href="#%s">%s</a>\n' % (g,g))
    f.write('<ul>')
    for m in sorted(departamentos[dep][g].keys()):
        f.write('<li><a href="#%s">%s</a></li>\n' % (m , m))
    f.write('</ul>')

    # Cada grupo
    for g in sorted(departamentos[dep].keys()):
        f.write('<a name="%s"><h2>%s</h2></a>\n' % (g,g))
        for m in sorted(departamentos[dep][g].keys()):
            f.write('<a name="%s"><img src="png/%s.png" alt="grafico de %s" /></a>\n' %
                    (m,
                     m.replace('/', '_')+'_'+g, m))
            f.write("<address>(c)lm productions 2008</address>")
    f.close()

if __name__ == '__main__':
    
    # lectura del fichero csv
    lineas = lee_csv()
    
    # estructura de datos
    departamentos = crear_estructura(lineas)
    
    #llenado de datos
    introduce_info(departamentos, lineas)
    resumen = resumen_datos(departamentos)
    
    # generación de gráficos
    hazmeGraficos(departamentos, resumen)
    creaHtmls(departamentos)








