# -*- encoding: utf-8 -*-

from pprint import pprint
import csv
import os

BASE_DOCS = 'Docum_SGC_obligatoria'

def convierte():
  
    reader = csv.reader(open("esquema.csv", "rb"))
    
    documentacion =[]
    
    for f in reader:
        documentacion.append(f)
    
    
    doc = [d for d in documentacion if d[0].strip()]
    
    doc = doc[1:]
    
    
    
    proc = {}
    for d in doc:
        if not d[-1]:
            proc[d[0].strip().decode('utf-8')] = []
    
    for d in doc:
        if d[-1]:
            p = {}
            p['nombre'] = d[0].strip().decode('utf-8')
            p['codigo'] = d[-2].strip().decode('utf-8')
            p['tipo'] = d[-1].strip().decode('utf-8')
            p['ruta'] = dameRuta(BASE_DOCS, p['codigo'])
            proc[cosa].append(p)
        else:
            cosa=d[0].strip().decode('utf-8')
    
    
    orden = []
    for d in doc:
        if not d[-1]:
            orden.append(d[0].strip().decode('utf-8'))
    return proc, orden

    



def creaDoc(nombre, lista):
    f = open(nombre, 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<ResultSet>\n')
    for el in lista:
        f.write('<Result>\n')
        f.write('<nombre>%s</nombre><codigo>%s</codigo><tipo>%s</tipo>' % (el['nombre'], el['codigo'], el['tipo']))
        f.write('</Result>')
    f.write('</ResultSet>')
    f.close()


def creaPagina(nombre='indice.html'):
    """ crea la página principal de documentacion
    """
    from genshi.template import TemplateLoader
    codigos = [(u'Anexo', u'ANX'), (u'Doc. de referencia', u'DIR'), 
               (u'Formato', u'F'), (u'Ficha de proceso', u'FP'), 
               (u'Instrucción', u'I'), (u'Manual de Calidad', u'MC'), 
               (u'Proc. General', u'PG')]

    loader = TemplateLoader(os.path.join(os.path.dirname(__file__), 'plantillas'))
    tmpl = loader.load('index.html')
    proc, orden = convierte()
    print tmpl.generate(title=u'Documentación sistema de calidad', orden=orden, proc=proc, codigos=codigos).render('html', doctype='html')
    

def dameRuta(base, nombre):
    """Devuelve la ruta en unicode de un archivo.
    El archivo es el nombre del archivo sin extensión que aparecerá en
    la tabla"""

    for root, dirs, files in os.walk('Docum_SGC_obligatoria'):
	for f in files:
		if nombre in f:
			return os.path.join(root, f).decode('utf-8')

def codigos():
    reader = csv.reader(open("codigos.csv", "rb"))
    cods = []
    for l in reader:
        cods.append((l[0].decode('utf-8'), l[-1].decode('utf-8')))
    return cods
                    

def creaXml():
    proc, orden = convierte()
    docs = u'<docCalidad>\n'
    listaDocs=[]
    for el in orden:
        for doc in proc[el]:
            listaDocs.append(u'<doc \ntipo="%s" \nruta="%s" \nbloque="%s">\n%s\n</doc>' % (doc['tipo'], doc['ruta'],el, doc['nombre']))
    docs = docs + u'\n'.join(listaDocs) + u'\n</docCalidad>'
    open('calidad.xml', 'w').write(docs.encode('utf-8'))
            
            
            

    

    
if __name__ == '__main__':
    proc, orden = convierte()
    #creaDoc('uno.xml', proc[orden[0]])
    #creaPagina()
    #print proc 
    #print codigos()
    creaXml()

