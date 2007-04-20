// $Id$

// Reserva y liberación de memoria

#include <stdio.h>
#include <stdlib.h>




int main(void)
{
    int dato, i, * pInt;
    FILE * f;
    
    f = fopen("numeros.dat", "wb");
    if (!f)
    {
           perror("numeros.dat");
           exit(1);
           }
    // escribo en fichero
    for (i=0; i<10000; i++)
    {   dato = i*2;
        fwrite(&dato, sizeof(dato), 1, f);
        }
    fclose(f);
    
    // apertura para lectura
    f = fopen("numeros.dat", "rb");
    if (!f)
    {
           perror("numeros.dat");
           exit(1);
           }
  
    // reservo espacio para 100 enteros
    // malloc --> stdlib
    pInt = (int *) malloc(sizeof(int) * 10000 );
    // uso calloc --> pInt = (int *) calloc(sizeof(int) , 100);
    // comprobar --> tratamiento de error
    if (! pInt)
    {
          perror("Puntero");
          system("pause");
          exit(1);
          }
    
    // inicializo
    i=0;
    while ( fread(&pInt[i], sizeof(dato), 100, f))  
    // fread(pInt +i , sizeof(dato), 100, f)
    // leo de 100 en 100
    {     printf("Leo 1 vez \n");
          i+=100; 
          }

        
    // mostrar al revés
    for (i=9999; i>=0; i--)
        printf("%d ", pInt[i]);
    printf("\n");
    
    // liberar memoria
    free(pInt);
    

  system("pause"); // Detiene la consola
  
}
