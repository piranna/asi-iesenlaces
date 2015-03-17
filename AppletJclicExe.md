# Docs #
  * http://clic.xtec.net/es/documents/jclic_cd.htm Uso de jclicplugin
  * http://clic.xtec.net/es/jclic/faqjclic.htm#faq7

  * http://senecux.wordpress.com/2007/04/12/jclic-con-exe-y-moodle/  Sobre la combinación eXe - moodle.

**http://clic.xtec.net/dist/jclic/jclicplugin.js* es más completo que el**jclicplugin.js**que viene con la distribución de jclic.**

# iDevice #
## java applet ##
```
<script 
    language="JavaScript" src="http://clic.xtec.net/dist/jclic/jclicplugin.js" 
    type="text/javascript">
</script>

<script language="JavaScript">
   setJarBase('http://clic.xtec.net/dist/jclic');
   writePlugin('http://clic.xtec.net/projects/geoclice/jclic/geoclice.jclic.zip', '800', '600');
</script>
```

## web externa / add as a link ##
```
http://clic.xtec.net/db/jclicApplet.jsp?project=http://clic.xtec.net/projects/geoclice/jclic/geoclice.jclic.zip&lang=es
```

## pure xhtml applet (object tag) ##

_firefox only_

```
<object classid="java:JClicApplet" 
	type="application/x-java-applet;version=1.3"
	archive="jclicapplet.jar,jclic.jar,activities.jar,utilities.jar,jclicxml.jar,jmfhandlers.jar,intl.jar,qt60.jar ,qt61.jar,soundspi.jar"
	height="600" width="800" 
	>
  <param name="codebase" value="." />
  <param name="activitypack" value="http://clic.xtec.net/projects/geoclice/jclic/geoclice.jclic.zip" />
  <strong>
    This browser does not have a Java Plug-in.
    <br />
    <a href="http://java.sun.com/products/plugin/downloads/index.html">
      Get the latest Java Plug-in here.
    </a>
  </strong>
</object>
```


## applet con ficheros locales (local files) ##
  * Añadir (Con el botón agreagar archivos) los archivos de JClic: jclicapplet.jar,jclic.jar,activities.jar,utilities.jar,jclicxml.jar,jmfhandlers.jar,intl.jar,qt60.jar ,qt61.jar,soundspi.jar y el archivo del activity pack que queremos ejecutar.

  * Modificar el applet para que lance el programa con un codebase local: 

&lt;param name="codebase" value="." /&gt;



**problemas**: control de anchura y altura.

## Examples ##
  * [exe\_jclic.elp](http://platea.pntic.mec.es/~jmorilla/moodle/exe_jclic.elp)
  * [jclics en scorm](http://platea.pntic.mec.es/~jmorilla/moodle/jclic_scorm.zip)
  * [dentro de moodle](http://moodle.ies-losenlaces.com/mod/scorm/view.php?id=777)