#Para trabajar con Documentos Word de Windows

# Trabajo con documentos de Word #

_Instalar extensiones win32all_: http://starship.python.net/crew/mhammond/win32/

```
import win32com.client
word = win32com.client.Dispatch('Word.Application')

doc = word.Documents.Open(r'c:\test.doc')

print doc.Content.Text
```