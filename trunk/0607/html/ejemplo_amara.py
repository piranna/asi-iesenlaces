Python 2.5 (r25:51908, Sep 19 2006, 09:52:17) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2      ==== No Subprocess ====
>>> import amara
>>> help(amara)
Help on package amara:

NAME
    amara - #Module amara

FILE
    c:\python25\lib\site-packages\amara\__init__.py

PACKAGE CONTENTS
    __config__
    bindery
    binderytools
    binderyxpath
    dateutil_standins
    domtools
    flextyper
    pyxml_standins
    saxtools
    scimitar
    trimxml

FUNCTIONS
    parse(source, uri=None, rules=None, binderobj=None, prefixes=None, validate=False, binding_classes=None)
        Convenience function for parsing XML.  Use this function with a single
        argument, which is a string (not Unicode object), file-like object
        (stream), file path or URI.
        Returns a document binding object.
        
        Only use this function to parse self-contained  XML (i.e. not requiring
        access to any other resource).  For example, do not use it for XML with
        external entities.  If you get URI resolution errors, pass in a URI
        parameter.
        
        uri - establish a base URI for the XML document entity being parsed,
              required if source is a string or stream containing XML that
              uses any external resources.  If source is a path or URI, then
              this parameter, if given, is ignored
        rules - a list of bindery rule objects to fine-tune the binding
        binderobj - optional binder object to control binding details,
                    the default is None, in which case a binder object
                    will be created
        prefixes - dictionary mapping prefixes to namespace URIs
                   the default is None

DATA
    PI_BINDING = 'http://uche.ogbuji.net/tech/4suite/amara/reserved/pi-bin...
    RESERVED_URI = 'http://uche.ogbuji.net/tech/4suite/amara/reserved/'
    __version__ = '1.2.0.1'

VERSION
    1.2.0.1


>>> import os
>>> os.getcwd()
'C:\\Documents and Settings\\Profesor\\Escritorio\\a2007\\html'
>>> os.listdir('.')
['.svn', 'caja', 'css', 'cv.html', 'ej_formulario.html', 'Etiquetas de html.html', 'flotar.html', 'formulario.html', 'images', 'indice.html', 'Lista de alumnos.html', 'meditaciones.html', 'nacho.jpg', 'paginaconestilo.html', 'test_amara.py']
>>> doc = amara.parse('Lista de alumnos.html')
>>> doc = amara.parse('Lista de alumnos.html')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    doc = amara.parse('Lista de alumnos.html')
  File "\PREFIX\Lib\site-packages\amara\__init__.py", line 64, in parse
  File "\PREFIX\Lib\site-packages\amara\binderytools.py", line 99, in bind_file
  File "\PREFIX\Lib\site-packages\amara\binderytools.py", line 78, in bind_uri
  File "C:\Python25\lib\site-packages\amara\bindery.py", line 261, in read_xml
    parser.parse(input_source)
SAXParseException: file:///C:/Documents%20and%20Settings/Profesor/Escritorio/a2007/html/Lista%20de%20alumnos.html:5:32: mismatched tag
>>> doc = amara.parse('Lista de alumnos.html')
>>> doc.xml()
'<?xml version="1.0" encoding="UTF-8"?>\n<html>\n<!--   namespace: xmlns="http://www.w3.org/1999/xhtml" -->\n\t<head><title>Lista de alumnos</title>\n\t</head>\n\t<body>\n\t\t<h1>Lista de alumnos de clase</h1>\n\t\t<ol>\n\t\t\t<li>Juan Alvarez</li>\n\t\t\t<li>Pedro Martinez</li>\n\t\t\t<li>Ana Ramos</li>\n\t\t\t<li>Clara Rodriguez</li>\n\t\t</ol>\n\t\t<img src="http://www.ies-losenlaces.com/ci/theme/formal_white/logo_small.jpg" style="width: 164px; height: 50px;" alt="ies los enlaces - logo"/>\n\t\t<div class="contenedor">\n\t\t\t<p>Div de clase contenedor</p>\n\t\t</div>\n\t\t<div class="otro">\n\t\t\t<p>Div de clase otro</p>\n\t\t</div>\n\t</body>\n</html>'
>>> print doc.xml()
<?xml version="1.0" encoding="UTF-8"?>
<html>
<!--   namespace: xmlns="http://www.w3.org/1999/xhtml" -->
	<head><title>Lista de alumnos</title>
	</head>
	<body>
		<h1>Lista de alumnos de clase</h1>
		<ol>
			<li>Juan Alvarez</li>
			<li>Pedro Martinez</li>
			<li>Ana Ramos</li>
			<li>Clara Rodriguez</li>
		</ol>
		<img src="http://www.ies-losenlaces.com/ci/theme/formal_white/logo_small.jpg" style="width: 164px; height: 50px;" alt="ies los enlaces - logo"/>
		<div class="contenedor">
			<p>Div de clase contenedor</p>
		</div>
		<div class="otro">
			<p>Div de clase otro</p>
		</div>
	</body>
</html>
>>> f = open('copia.html', 'w')
>>> print doc.xml(stream=f)
None
>>> print doc.xml(stream=f)
None
>>> f.close()
>>> print "El titulo del documento es", doc.html.head.title
El titulo del documento es Lista de alumnos
>>> print "El titulo del documento es '%s'" %  doc.html.head.title
El titulo del documento es 'Lista de alumnos'
>>> print "El encabezado del documento es '%s'" %  doc.html.body.h1
El encabezado del documento es 'Lista de alumnos de clase'
>>> print "Los alumnos de la lista son: ", doc.html.body.ol
Los alumnos de la lista son:  
			Juan Alvarez
			Pedro Martinez
			Ana Ramos
			Clara Rodriguez
		
>>> doc.html.body.ol
<amara.bindery.ol object at 0x017A4C30>
>>> len(doc.html.body.ol)
1
>>> len(doc.html.body.ol.li)
4
>>> print "El número de alumnos de la lista es ", len(doc.html.body.ol.li)
El número de alumnos de la lista es  4
>>> print doc.html.body.ol.li
Juan Alvarez
>>> print doc.html.body.ol.li[1]
Pedro Martinez
>>> print doc.html.body.ol.li[2]
Ana Ramos
>>> for numero , al in doc.html.body.ol.li:
KeyboardInterrupt
>>> numero = 1
>>> for al in doc.html.body.ol.li:
	print 'Alumno número %d: %s' % (numero, al)
	numero += 1

	
Alumno número 1: Juan Alvarez
Alumno número 2: Pedro Martinez
Alumno número 3: Ana Ramos
Alumno número 4: Clara Rodriguez
>>> doc.html.body.img
<amara.bindery.img object at 0x0144C630>
>>> doc.html.body.img.src
u'http://www.ies-losenlaces.com/ci/theme/formal_white/logo_small.jpg'
>>> import urllib
>>> imagen = urllib.urlopen(doc.html.body.img.src)
>>> mi_imagen = open('logo.jpg', 'wb')
>>> mi_imagen.write(imagen.read() )
>>> mi_imagen.close()
>>> imagen
<addinfourl at 27470184 whose fp = <socket._fileobject object at 0x01A3D6C0>>
>>> for d in doc.xml_xpath('u//div'):
	print d

	
>>> doc.xml_xpath('u//div')
[]
>>> doc.xml()
'<?xml version="1.0" encoding="UTF-8"?>\n<html>\n<!--   namespace: xmlns="http://www.w3.org/1999/xhtml" -->\n\t<head><title>Lista de alumnos</title>\n\t</head>\n\t<body>\n\t\t<h1>Lista de alumnos de clase</h1>\n\t\t<ol>\n\t\t\t<li>Juan Alvarez</li>\n\t\t\t<li>Pedro Martinez</li>\n\t\t\t<li>Ana Ramos</li>\n\t\t\t<li>Clara Rodriguez</li>\n\t\t</ol>\n\t\t<img src="http://www.ies-losenlaces.com/ci/theme/formal_white/logo_small.jpg" style="width: 164px; height: 50px;" alt="ies los enlaces - logo"/>\n\t\t<div class="contenedor">\n\t\t\t<p>Div de clase contenedor</p>\n\t\t</div>\n\t\t<div class="otro">\n\t\t\t<p>Div de clase otro</p>\n\t\t</div>\n\t</body>\n</html>'
>>> doc.xml_xpath('u//body')
[]
>>> doc.xml_xpath('u//body')
KeyboardInterrupt
>>> doc.xml_xpath(u'//div')
[<amara.bindery.div object at 0x0144C290>, <amara.bindery.div object at 0x0144C550>]
>>> for d in doc.xml_xpath(u'//div'):
	print d

	

			Div de clase contenedor
		

			Div de clase otro
		
>>> divs = doc.xml_xpath(u'//div')
>>> divs
[<amara.bindery.div object at 0x0144C290>, <amara.bindery.div object at 0x0144C550>]
>>> dir(divs[0])
['__class__', '__cmp__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__', '__len__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__str__', '__unicode__', '__weakref__', '_attributes', '_childNodes', '_localName', '_namespaceURI', '_parentNode', '_prefix', '_rootNode', '_xpathAttributes', 'attributes', 'childNodes', u'class_', 'docIndex', 'getAttributeNS', 'is_attribute', 'localName', 'namespaceURI', 'next_elem', 'nodeName', 'nodeType', 'ownerDocument', u'p', 'parentNode', 'prefix', 'rootNode', 'xml', 'xml_append', 'xml_append_fragment', 'xml_attributes', 'xml_child_elements', 'xml_child_text', 'xml_children', 'xml_clear', 'xml_create_element', 'xml_doc', 'xml_ignore_members', 'xml_index_on_parent', 'xml_insert_after', 'xml_insert_before', 'xml_naming_rule', 'xml_parent', 'xml_properties', 'xml_remove_child', 'xml_remove_child_at', 'xml_set_attribute', 'xml_text_content', 'xml_xpath', 'xml_xslt', 'xpathAttributes']
>>> for d in doc.xml_xpath(u'//div'):
	print d.class_

	
contenedor
otro
>>> for d in doc.xml_xpath(u'//div'):
	if  d.class_ == 'contenedor':
		print d

		

			Div de clase contenedor
		
>>> for d in doc.xml_xpath(u'//div[@class="contenedor"]'):
		print d

		

			Div de clase contenedor
		
>>> 
