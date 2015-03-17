# ¿Qué es un cgi? #

Common Gateway Interface (abreviado CGI) es una tecnología que permite a un cliente (explorador web) solicitar datos de un programa ejecutado en un servidor web. CGI especifica un estándar para transferir datos entre el cliente y el programa.

http://es.wikipedia.org/wiki/Common_Gateway_Interface

# Introducción #
## Preparación del entorno ##
PreparacionEntornoCgiUbuntu

## Primer cgi en python ##

### cgi-bin/test.py ###
```
import cgi  # Importa CGI

##Devolvera esto al cliente web

print "Content-type: text/html" ##Importante
print
print "<h1>Hola, mundo</h1>
```
### Hacer ejecutable el archivo para apache ###
`$ chmod +x test.py`

El archivo tiene que tener permisos de lectura y ejecución para apache (`www-data`).

### Abrimos con el navegador el archivo que acabamos de crear: ###
```
http://localhost/~asi/cgi-bin/test.py
```

### En caso de error podemos ver el log de errores de Apache: ###
```
asi@ubuntu-12:~$ tail -f /var/log/apache2/error.log
```