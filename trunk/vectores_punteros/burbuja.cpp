// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAM 10
#define LON 40

void insercion(int v[], int N)
{
     int i, k;
     int aux;
     for (i=1; i< N; i++)
     {
         aux = v[i];
         for(k=i-1; k>=0 && v[k]>aux; k--)
                   v[k+1] = v[k];
         v[k+1] = v[k];
         }
}

void burbuja_c(char v[][LON], int N)
// para ordenar cadenas de caracteres
// parámetros: vector y dimensión del vector (entero)
// v: entrada y salida
// cuidado con la declaracion de aux
{
     int i, k;  // índices que guían el proceso de comparaciones
     char aux[LON];   // del tipo de lo que ordenamos
     for(i=1; i<N; i++)             // bucle de comparaciones
         for(k=0; k<N-i;  k++)
         
            if(strcmp(v[k],v[k+1]) > 0 )         // comparación : menor a mayor
            {                       // permutación de la pareja
                strcpy(aux,v[k]);           // cuidado con las cadenas de caracteres
                strcpy(v[k],v[k+1]);
                strcpy(v[k+1],aux);
            }
}

void burbuja(int v[], int N)
// parámetros: vector y dimensión del vector (entero)
// v: entrada y salida
{
     int i, k;  // índices que guían el proceso de comparaciones
     int aux;   // del tipo de lo que ordenamos
     for(i=1; i<N; i++)             // bucle de comparaciones
         for(k=0; k<N-i;  k++)
         
            if(v[k]<v[k+1])         // comparación : menor a mayor
            {                       // permutación de la pareja
                aux=v[k];           // cuidado con las cadenas de caracteres
                v[k]=v[k+1];
                v[k+1]=aux;
            }
}

void burbujaf(float v[], int N)
// parámetros: vector y dimensión del vector (float)
// v: entrada y salida
{
     int i, k;  // índices que guían el proceso de comparaciones
     float aux;   // del tipo de lo que ordenamos
     for(i=1; i<N; i++)             // bucle de comparaciones
         for(k=0; k<N-i;  k++)
         
            if(v[k]<v[k+1])         // comparación : menor a mayor
            {                       // permutación de la pareja
                aux=v[k];           // cuidado con las cadenas de caracteres
                v[k]=v[k+1];
                v[k+1]=aux;
            }
}


int main(void)
{
    int lista[10] = {3,4,5,6,2,8,5,9,7,1};
    float listaf[10] = {3.0,4,5,6,2,8,5,9,7,1};
    char lista_nombres[TAM][LON] = {"Pedro", "Maria", "Ana", "Carmen"};
    int i;
    burbuja_c(lista_nombres, 4);   // ordena el vector   
    for (i=0; i<TAM; i++)
        printf("%s - ", lista_nombres[i]);
    printf("\n");
    
  system("pause"); // Detiene la consola
  
}






