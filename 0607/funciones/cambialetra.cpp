// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cambia(char * cadena, char letra)
// void cambia(char cadena[], char letra)
{
     int i, tam;
     tam = strlen(cadena);
     for (i=0; i<tam; i++)
         if (cadena[i] == letra)
            cadena[i] = '?';
}

void cambia_v2(char * cadena, char letra)
// voy a usar strchr
{
     char * aux; // puntero a char para guardar la dirección de la letra
     aux = cadena;
     while( aux = strchr(aux, letra) )  // termina cuando strchr devuelve NULL
            {
            // printf("--> %s\n", aux);   // comprobación de strchr
            *aux = '?';  // aux[0] = '?';
            aux += 1;
            }
}

 
int main(void)
{   
    char frase[]="Buenos días, señoras y señores";
    printf("%s -> ", frase);
    cambia(frase, 's');
    printf("%s\n", frase);
    cambia_v2(frase, 'a');
    printf("%s\n", frase);
    system("pause"); // Detiene la consola
  
}
