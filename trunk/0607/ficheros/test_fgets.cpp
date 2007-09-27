// $Id$

// Comparación de lecturas con gets y fgets

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 8

void letras(char cadena[])
{
     int tam, i;
     tam = strlen(cadena);
     for (i=0; i<tam; i++)
         printf("%d - ", cadena[i]);
     printf("\n");
     }


int main(void)
{
    char test1[TAM], test2[TAM];
    
    printf("Leer con gets -->");
    gets(test1);
    printf("Leer con fgets -->");
    fgets(test2,TAM, stdin);
    if (test2[strlen(test2) -1] == '\n')  // -1 porque empieza a numerar de 0 ...
       test2[strlen(test2) -1] = '\0';
       
    
    printf("cadena1: %s.\ncadena2: %s.\n", test1, test2);
    letras(test1);
    printf("**********************\n");
    letras(test2);
       

  system("pause"); // Detiene la consola
  
}










