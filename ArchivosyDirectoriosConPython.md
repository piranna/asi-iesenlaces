# Trabajando con archivos y directorios con Python #

## Listado de archivos en un directorio ##

Para buscar todos los archivos con una extensión, por ejemplo .jpg:
```
import glob
lista = glob.glob("*.jpg")
```
Para listar todos los archivos de un directorio:
```
import os
ficheros = os.listdir('/home/alumno/ejercicios/python') # linux
ficheros = os.listdir(r'c:\Documents and Settings\alumno\Escritorio\ejercicios\python') #windows: cuidado con el caracter \
```
Directorio actual:
```
os.getcwd()
os.curdir
```

## Tipos de ficheros ##
```
print michero, 'es un', 
if os.path.isfile(mifichero):
    print 'fichero'
if os.path.isdir(mifichero):
    print 'directorio'
if os.path.islink(mifichero):
    print 'enlace'
```

## Último acceso a un fichero ##
```
ultimo_acceso = os.path.getatime('foto.jpg')
ultima_modificacion = os.path.getmtime('foto.jpg')
tiempo_en_dias = (time.time()- ultimo_acceso)/ (60*60*24)
print tiempo_en_dias
```

## Eliminar ficheros y directorios ##
```
os.remove('mifoto.jpg')
for foto in glob.glob('*.jpg') + glob.glob('*.tif'):
    os.remove(foto)
```
Eliminar directorio:
```
import shutil
shutil.rmtree('midirectorio')
```

## Copiar y renombrar ficheros ##
```
import shutil
shutil.copy(mifichero, copiafichero)

# copia también tiempo de último acceso y última modificación
shutil.copy2(mifichero, copiafichero)

# copia un árbol de directorios
shutil.copytree(raiz_de_directorio, copia_directorio)
```

## Manipulando los paths y nombres ##
Rutas
```
>>> os.path.split('/home/alumno/python/ejercicios/ej1.py')
('/home/alumno/python/ejercicios', 'ej1.py')
>>> os.path.basename('/home/alumno/python/ejercicios/ej1.py')
'ej1.py'
>>> os.path.dirname('/home/alumno/python/ejercicios/ej1.py')
'/home/alumno/python/ejercicios'
```
Extensiones
```
>>> os.path.splitext('pelicula.avi')
('pelicula', '.avi')
```

## Crear y moverse entre directorios ##
```
directorioOriginal = os.getcwd()
directorio = os.path.join(os.pardir, 'miNuevoDir')
if not os.path.isdir(directorio):
    os.mkdir(directorio)
os.chdir(directorio)
...
os.chdir(directorioOriginal) # vuelve al directorio inicial
os.chdir(os.environ['HOME']) # cambia al directorio home
```