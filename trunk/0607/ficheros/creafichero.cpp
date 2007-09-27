// $Id$

// Crea un fichero con lo que introducimos de teclado


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 256

int main(void)
{
    FILE *fesc; // ficheros de lectura y escritura
    char nombre[TAM]; // nombre del fichero
    char dato; // copia byte a byte
    
    // pedir fichero 
    printf("Introduzca fichero : ");
    fgets(nombre, TAM, stdin);
    if (nombre[strlen(nombre)-1] == '\n')
       nombre[strlen(nombre)-1] = '\0';

    // abrir fichero
    if (!(fesc = fopen(nombre, "w") ) )
    {
               perror("fopen");
               system("pause");
               exit(1);
    }
    
    printf("Introduzca el contenido del fichero (ctrl+Z para terminar):\n");
    // bucle lectura / escritura
    dato = fgetc(stdin);
    while(!feof(stdin))
    {
        fputc(dato, fesc);
        dato = fgetc(stdin);
    }
        
    // cerrar ficheros
    fclose(fesc);
    
  system("pause"); // Detiene la consola
  
}








