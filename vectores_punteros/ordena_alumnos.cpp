// $Id$

/*
Escribir todos los algoritmos de ordenacion para el siguiente vector, con los criterios que se indican a
continuacion:
struct reg {
char nombre[50];
int edad;
float nota;
} vec[100];
* Ordenarlo ascendentemente por nombre
* Ordenarlo descendentemente por nota
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NALUMNOS 100
#define TAM 50

struct reg {
       char nombre[TAM];
       int edad;
       float nota;
       };

void ordena_nota(struct reg v[], int N)
{
     int i, k;  // índices que guían el proceso de comparaciones
     struct reg aux;   // del tipo de lo que ordenamos
     for(i=1; i<N; i++)             // bucle de comparaciones
         for(k=0; k<N-i;  k++)
         
            if(v[k].nota > v[k+1].nota)         // comparación : menor a mayor
            {                       // permutación de la pareja
                aux=v[k];           // cuidado con las cadenas de caracteres
                v[k]=v[k+1];
                v[k+1]=aux;
            }
     }

void ordena_nombre(struct reg v[], int N)
{
     int i, k;  // índices que guían el proceso de comparaciones
     struct reg aux;   // del tipo de lo que ordenamos
     for(i=1; i<N; i++)             // bucle de comparaciones
         for(k=0; k<N-i;  k++)
         
            if(strcmp(v[k].nombre, v[k+1].nombre)  > 0)       // comparación : menor a mayor
            {                       // permutación de la pareja
                aux=v[k];           // cuidado con las cadenas de caracteres
                v[k]=v[k+1];
                v[k+1]=aux;
            }
     }

int main(void)
{
    struct reg alumnos[NALUMNOS] = {{"Ana", 19, 4.5}, 
                                   {"Jesus",21, 5.5},
                                   {"Miguel", 20, 7.5},
                                   {"Carmen", 18, 9.6},
                                   };
    int i;
    
    ordena_nombre(alumnos, 4);
    for (i=0; i<4; i++)
        printf("%-12s  %4d  %6.2f\n" , alumnos[i].nombre, alumnos[i].edad , 
                       alumnos[i].nota);
        
    
  system("pause"); // Detiene la consola
  
}
