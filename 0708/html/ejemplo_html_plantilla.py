import webbrowser

# abrir fichero escritura (texto)
f = open('pagina2.html', 'w')

plantilla = """<html>
    <head>
        <title>%s</title>
    </head>
    <body>
        %s
    </body>
    </html>
"""

#inicio

titulo = "Primera pagina"
contenido = "<h1>Otro ejemplo diferente</h1>"

f.write(plantilla % (titulo, contenido) )

f.close()

webbrowser.open('pagina2.html')

