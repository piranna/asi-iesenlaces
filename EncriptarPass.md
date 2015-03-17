# Encriptar Contraseñas #

**md5**
```
import md5
clave = raw_input( "Introduzca la contraseña: " )
print md5.new(clave).hexdigest()
```

**md5 con semilla**
```
import md5

clave = "mibuenaclave"
semilla = "1Ha7"
hash = md5.new(semilla + clave).hexdigest()
print "%s:%s" % (semilla, hash) # guardar esta cadena
```

**sha256**
```
import hashlib
print hashlib.sha256('este es mipassword').hexdigest()

'8875db0614a5eb7fdafcd71695ccc0d95fd81b4fe58e0899b96ee68ca9bfbc4a'
```

## Documentación ##
  * http://docs.python.org/lib/crypto.html
## Ejemplos de uso ##
  * http://springpython.python-hosting.com/browser/trunk/src/springpython/security/providers/encoding.py