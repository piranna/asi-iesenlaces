// $Id$

// métodos de ordenación: método de inserción

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 40

struct persona{
       char nombre[TAM];
       int edad;
       };

void insercion(int v[], int N)
{
     int i, k, aux;
     for(i=1; i<N; i++)
     {
         aux=v[i];
         for(k=i-1; k>=0 && v[k]>aux; k--)
            v[k+1]=v[k];
         v[k+1]=aux;
     }
}

void insercion_str(char v[][40], int N)
{
     int i, k;
     char aux[40];
     for(i=1; i<N; i++)
     {
         strcpy(aux,v[i]);
         for(k=i-1; k>=0 && (strcmp(v[k],aux) > 0); k--)
            strcpy(v[k+1],v[k]);
         strcpy(v[k+1], aux);
     }
}


void ordena_persona(struct persona per[], int N)
// ordena la estructura ascendente por los nombres
{
     int i, k;
     struct persona aux;
     for(i=1; i<N; i++)
     {
         aux = per[i];
         // for(k=i-1; k>=0 && (strcmp(per[k].nombre, aux.nombre) < 0); k--)  //orden por nombre de mayor a menor
         for(k=i-1; k>=0 && (per[k].edad > aux.edad) ; k--)  // orden por edad
            per[k+1] = per[k];
         per[k+1] = aux;
     }
}

int main(void)
{
    int vector[10] = {4,5,7,2,8,9,3,5,6,11};   //vector de 10 enteros
    char nombres[10][40] = {"Marcos", "Juan", "Maria", "Ana", "Pilar", "Miguel",
                           "Elena"}; // 7 nombres
    struct persona v_pers[10] = {"Ana", 6, "Mario", 20, "Juan", 21};
    
    int i;
    // aplicamos la función
    insercion(vector, 10);

    // ver resultado
    for (i=0; i< 10; i++)
        printf("%d, ", vector[i]);
    printf("\n");
    
    insercion_str(nombres, 7);
    for (i=0; i< 7; i++)
        printf("%s, ", nombres[i]);
    printf("\n");

    ordena_persona(v_pers, 3);
    for (i=0; i< 3; i++)
        printf("%-10s (%d)\n", v_pers[i].nombre, v_pers[i].edad);
    printf("\n");
    
  system("pause"); // Detiene la consola
  
}
