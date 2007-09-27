// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 50

int main(void)
{

    char nombre[TAM] = "Me gusta trabajar con punteros", *pchar;
    int i, max;
    pchar = nombre;
    max = strlen(nombre);
    /*
    for (i=0; i<max; i++)
        printf("%s\n", pchar+i);

    for (i=max-1; i>=0; i--)
        printf("%s\n", pchar+i);
        
    for (i=max; i>=0; i--)
    {   
        *(pchar+i) = '\0'; /// modifico la cadena de caracteres ********
        printf("%s\n", pchar);
    }
*/
    // otra forma
    pchar = nombre+max;  // pchar apunta al final de la cadena: al NULL
    for (; pchar >= nombre; pchar--)
     {   
        *pchar = '\0'; /// modifico la cadena de caracteres ********
        printf("%s\n", nombre);
    }
    
    
    system("pause"); // Detiene la consola
  
}








