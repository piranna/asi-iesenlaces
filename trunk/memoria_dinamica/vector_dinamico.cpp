// $Id$

// Reserva y liberación de memoria

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int dato, i, * pInt;
    
    // reservo espacio para 100 enteros
    // malloc --> stdlib
    pInt = (int *) malloc(sizeof(int) * 1000000000000L);
    // uso calloc --> pInt = (int *) calloc(sizeof(int) , 100);
    // comprobar --> tratamiento de error
    if (! pInt)
    {
          perror("Puntero");
          system("pause");
          exit(1);
          }
    
    // inicializo
    for (i=0; i<100; i++)
        pInt[i] = i*i;
        
    // mostrar al revés
    for (i=99; i>=0; i--)
        printf("%d ", pInt[i]);
    printf("\n");
    
    // liberar memoria
    free(pInt);
    

  system("pause"); // Detiene la consola
  
}
