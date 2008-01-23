import webbrowser

# abrir fichero escritura (texto)
f = open('pagina.html', 'w')
#inicio
f.write('<html>\n')
# head
f.write('<head><title>Primera pagina</title></head>\n')
# body
f.write('<body><h1>Saludos desde clase</h1>')
f.write('<ul>')
for n in range(1, 11):
    f.write('<li>'+'alumno '+str(n) + '</li>\n')
f.write('</ul>')
f.write('</body>\n')
f.write('</html>\n')
f.close()

webbrowser.open('pagina.html')

