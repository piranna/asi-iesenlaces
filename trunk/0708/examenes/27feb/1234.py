# -*- coding: utf-8 -*-

def listadoAlumnos(listaAlumnos, curso, grupo=0):
    """
    Entrada: una lista de alumnos como la indicada anteriormente, el nombre de un curso y opcionalmente el número de un grupo.
    Devuelve una lista con los datos de los alumnos del curso y grupo indicados. Si no se indica grupo, devolverá todos los alumnos del curso indicado.
    """
    
    resultado = []
    for alumno in listaAlumnos:
        if grupo:
            if alumno[1] == curso and alumno[2]==grupo:
                resultado.append(alumno)
        else:
            if alumno[1] == curso:
                resultado.append(alumno)
    return resultado


def media(notas):
    return sum(notas)/len(notas)

def alumnoMedia(listaAlumnos):
    """
    Entrada: una lista de alumnos como la indicada anteriormente.
    Devuelve una lista de parejas: nombre de alumno, media de las notas.
    """
    resultado = []
    for al in listaAlumnos:
        resultado.append([al[0], media(al[-1])])
    return resultado

def listadoDeAlumnosAprobados(rutaFichero, listaAlumnos, curso, grupo=0):
    """
    Entrada: una lista de alumnos como la indicada anteriormente, la ruta de un fichero, el nombre de un curso y opcionalmente el número de un grupo.
    Salida: crea un fichero con los datos de los alumnos del curso que aprueban. Si no se especifica grupo, se refiere a todo el curso. Los datos se grabarán con la siguiente estructura:
    nombre del alumno; media de las asignaturas
    nombre del alumno; media de las asignaturas
    nombre del alumno; media de las asignaturas
    """
    f = open(rutaFichero, 'w')
    alumnos = listadoAlumnos(listaAlumnos, curso, grupo)
    medias = alumnoMedia(alumnos)
    for al in medias:
        if al[1] >= 5:
            f.write("%s;%d\n" % (al[0], al[1]))
    f.close()

def mejorNota(rutaFichero):
    """
    Entrada: una ruta de un fichero que tiene la estructura creada anteriormente.
    Salida: imprime en pantalla el alumno (o alumnos) que tienen la mejor nota con el siguiente formato: Nombre de alumno: nota.
    """
    f = open(rutaFichero)
    mejores = []
    mejor = -1  # inicializado con dato no válido
    for linea in f:
        nombre, nota = linea.split(';')
        nota = int(nota)
        if nota == mejor:
            mejores.append([nombre, nota])
        if nota > mejor:
            mejor = nota
            mejores = [[nombre, nota]]
    for nombre, nota in mejores:
        print nombre,'-->',  nota


if __name__ == '__main__':
    # datos de test
    lista_alumnos = [
        ["Pérez, Juan", "ASI", 1, [4, 5, 8, 3] ],
        ["Alvarez, Maria", "ESI", 2, [8,6,5,9,4]],
        ["Rivas, Ana", "ASI", 1, [3,4,5]],
        ["Marcos, Carlos", "ASI", 2, [9,9,9]],
        ["Vera, Carmen", "ASI", 2, [8,9,10]]
        ]

    # funciones de test
    # alumnos de ASI
    print listadoAlumnos(lista_alumnos, "ASI")
    print 
    # alumnos de 1º de ASI
    print listadoAlumnos(lista_alumnos, "ASI",1)
    print 
    # media de todos los alumnos
    print alumnoMedia(lista_alumnos)
    print
    # media de los de ASI
    print alumnoMedia(listadoAlumnos(lista_alumnos, "ASI"))
    print 
    # listado aprobados
    listadoDeAlumnosAprobados('aprueban_Asi.txt', lista_alumnos, 'ASI')

    mejorNota('aprueban_Asi.txt')
    
    
    
       
        
