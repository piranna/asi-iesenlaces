# Preparación del entorno #
## Configurar apache + userdir ##
```
asi@ubuntu-12:~$ sudo nano /etc/apache2/mods-available/userdir.conf 
```

Añadimos al '''userdir.conf''' de apache estas lineas:
```
        <Directory /home/*/public_html/cgi-bin/> 
                Options ExecCGI 
                SetHandler cgi-script 
        </Directory> 
```
```
Control+X: Guardar? Si
asi@ubuntu-12:~$ sudo apache2ctl restart 
asi@ubuntu-12:~$ cd public_html 
asi@ubuntu-12:~/public_html$ mkdir cgi-bin 
asi@ubuntu-12:~/public_html$ cd cgi-bin 
```

## Instalamos Idle ##
(para editar el código python)
```
asi@ubuntu-12:~/public_html/cgi-bin$ sudo aptitude install idle  // Instala Idle
asi@ubuntu-12:~/public_html/cgi-bin$ idle // Abre la consola de Python
```