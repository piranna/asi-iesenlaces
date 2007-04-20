// $Id$

// copia un fichero en otro

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 256

int main(void)
{
    FILE *flec, *fesc; // ficheros de lectura y escritura
    char nombre[TAM]; // nombre del fichero
    char dato; // copia byte a byte
    
    // pedir fichero lectura
    printf("Introduzca fichero origen: ");
    fgets(nombre, TAM, stdin);
    if (nombre[strlen(nombre)-1] == '\n')
       nombre[strlen(nombre)-1] = '\0';

    // abrir fichero lectura
    if (!(flec = fopen(nombre, "rb") ) )
    {
               perror("fopen");
               system("pause");
               exit(1);
    }
    // pedir fichero backup
    printf("Introduzca fichero destino: ");
    fgets(nombre, TAM, stdin);
    if (nombre[strlen(nombre)-1] == '\n')
       nombre[strlen(nombre)-1] = '\0';
       
    // abrir fichero backup
    if (!(fesc = fopen(nombre, "wb") ) )
    {
               perror("fopen");
               system("pause");
               exit(1);
    }
    
    // bucle lectura / escritura
    dato = fgetc(flec);
    while(!feof(flec))
    {
        fputc(dato, fesc);
        dato = fgetc(flec);
    }
        
    // cerrar ficheros
    fclose(flec);
    fclose(fesc);
    
  system("pause"); // Detiene la consola
  
}








